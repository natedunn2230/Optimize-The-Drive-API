import requests
import config

def get_distance_matrix(locations, type="fastest;car;"):
    """
        Distance between two geographical locations (denoted by lat, long)
        Returns {distance: number, travelTime: number, costFactor: number}
    """

    full_request = "{}?start0={}&destination0={}&mode=fastest;car&summaryAttributes=distance,traveltime&apiKey={}".format(config.MATRIX_URL, locations[0], locations[1], config.HERE_API_KEY)
    response = requests.get(full_request).json()

    return response['response']['matrixEntry'][0]['summary']

def get_address_by_location(lat, lng):
    """
        Get name of location based on latitude and longitude.
        Returns: {display_name: string}
    """
    request = "{}/{}?key={}&lat={}&lon={}&format=json".format(config.GEOCODE_URL, config.GEOCODE_REVERSE_PATH, config.GEOCODE_KEY, lat, lng)
    response = requests.get(request).json()
    return response

def get_address_by_name(name, limit):
    """
        Get location based off of address name.
        Returns: {name: string, lat: number, lng: number}
    """
    request = "{}/{}?key={}&q={}&type=json&limit={}".format(config.GEOCODE_URL, config.GEOCODE_SEARCH_PATH, config.GEOCODE_KEY, name, limit)
    response = requests.get(request).json()
    return response