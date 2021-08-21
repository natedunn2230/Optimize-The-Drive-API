import requests
def get_distance_matrix(api_key, locations, type="fastest;car;"):
    """
        Distance between two geographical locations (denoted by lat, long)
        Returns {distance: int, travelTime: int, costFactor: int}
    """

    REQUEST_URL = "https://matrix.route.ls.hereapi.com/routing/7.2/calculatematrix.json"
    full_request = REQUEST_URL + "?start0={}&destination0={}&mode=fastest;car&summaryAttributes=distance,traveltime&apiKey={}".format(locations[0], locations[1], api_key)
    response = requests.get(full_request).json()

    return response['response']['matrixEntry'][0]['summary']
    