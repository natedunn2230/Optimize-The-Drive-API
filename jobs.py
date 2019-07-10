from optimizer.distance_finder import find_distances
from optimizer.path_finder import run_genetic_algorithm
from config import GOOGLE_API_KEY


def compute_path(data_set):
    """
        Calls the genetic algorithm code to optimize the data set
    """
    find_distances(data_set, GOOGLE_API_KEY)
    optimized_path = run_genetic_algorithm()
    return optimized_path