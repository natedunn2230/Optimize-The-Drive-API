# import googlemaps
from itertools import combinations
from .path_finder import run_genetic_algorithm
from here_requests import get_distance_matrix
import sys
def find_distances(all_waypoints, api_key):
    """
        This function Finds the distance between each waypoint (by calling Google's Distance Matrix API)
        and stores the distance and duration between the two in a file.
    """
    # gmaps = googlemaps.Client(key=api_key)

    waypoint_distances = {}
    waypoint_durations = {}

    for (waypoint1, waypoint2) in combinations(all_waypoints, 2):
        try:
            response = get_distance_matrix(api_key, [waypoint1, waypoint2])
            # route = gmaps.distance_matrix(origins=[waypoint1],
            #     destinations=[waypoint2],
            #     mode="driving", # Change this to "walking" for walking directions,
            #                     # "bicycling" for biking directions, etc.
            #     language="English",
            #     units="metric")

            ##"distance" is in meters
            print(response)
            distance = response['distance']

            # "duration" is in seconds
            duration = response['travelTime']

            waypoint_distances[frozenset([waypoint1, waypoint2])] = distance
            waypoint_durations[frozenset([waypoint1, waypoint2])] = duration
        
        except Exception as e:
            print("Error with finding the route between %s and %s." % (waypoint1, waypoint2), e)

    with open("my-waypoints-dist-dur.tsv", "w") as out_file:
        out_file.write("\t".join(["waypoint1",
            "waypoint2",
            "distance_m",
            "duration_s"]))
        
        for (waypoint1, waypoint2) in waypoint_distances.keys():
            out_file.write("\n" +
                "\t".join([waypoint1,
                            waypoint2,
                            str(waypoint_distances[frozenset([waypoint1, waypoint2])]),
                            str(waypoint_durations[frozenset([waypoint1, waypoint2])])]))
