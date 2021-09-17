from app import app
from flask import jsonify, render_template, request
from rq.job import Job, NoSuchJobError
from worker import conn, queue
from .jobs import compute_path
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
        return jsonify({"err": "An error occurred during optimization."}), 400

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