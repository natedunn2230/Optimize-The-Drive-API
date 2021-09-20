from app import app
from flask import jsonify, render_template, request
from rq.job import Job, NoSuchJobError
from worker import conn, queue
from .jobs import compute_path
from .requests import get_address_by_name, get_address_by_location
import json

# ENTRY ROUTE
@app.route("/")
def entry():
    return render_template("welcome.html"), 200

# OPTIMIZER ROUTES
@app.route("/optimize", methods=["POST"])
def optimize():
    """
        Create a background task to calculate the optimal route between the points
        passed by the client
    """
    try:
        data = json.loads(request.data)

        if len(data) == 0:
            return jsonify({"err": "Key 'locations' is required for optimization."}), 400
        locations = data["locations"]

        if not isinstance(locations, list):
            return jsonify({"err": "Value for 'locations' must be array."}), 400

        if len(locations) < 2 or len(locations) > 5:
            return jsonify({"err": "Between two and five locations are required for optimization."}), 400

        job = queue.enqueue_call(func=compute_path, args=(locations,), result_ttl=600)

    except json.JSONDecodeError as jsonError:
        print(jsonError)
        return jsonify({"err": "Invalid json syntax."}), 500

    except Exception as error:
        print(error.with_traceback)
        return jsonify({"err": "An error occurred during optimization. {}".format(error)}), 500

    return jsonify({
        "msg": "Optimization started. Poll /optimize/result/<id> periodically for the result",
        "id": job.id
    }), 202

@app.route("/optimize/result/<job_id>", methods=["GET"])
def get_results(job_id):
    """
        Get the result of the job based on its id
    """
    try:
        job = Job.fetch(job_id, connection=conn)
        if job.is_finished:
            return jsonify({
                "status": "finished",
                "data": job.result
            }), 200
        elif job.is_failed:
            return jsonify({
                "status": "failed"
            }), 200
        else:
            return jsonify({
                "status": "in-progress"
            }), 200
    except NoSuchJobError:
        return jsonify({
            "msg": "job id does not exist"
        }), 404


# LOCATION QUERY ROUTES
@app.route("/locations", methods=["GET"])
def get_location():
    """
        Query location data by coord or name. If both types are given,
        then query by name is given priority
    """
    name = request.args.get("name")
    lat = request.args.get("lat")
    lng = request.args.get("lng")
    limit = request.args.get("limit")

    if name:
        loc_req = get_address_by_name(name, limit)
        try:
            format_data = [{"name": loc["display_name"], "lat": loc["lat"], "lng": loc["lon"]} for loc in loc_req] 
            return jsonify({"locations": format_data}), 200
        except (KeyError, TypeError):
            return jsonify({"locations": []}), 200
    elif lat and lng:
        loc_req = get_address_by_location(lat, lng)
        try:
            format_data = {
                "name": loc_req["display_name"], 
                "lat": loc_req["lat"],
                "lng": loc_req["lon"]
            }
            return jsonify({"locations": [format_data]}), 200
        except KeyError:
            return jsonify({"locations": []}), 200
    else:
        return jsonify({"msg": "parameters 'name' or 'lat'/'lng' required"}), 400