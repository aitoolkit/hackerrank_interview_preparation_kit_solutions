from topics.graphs.roads_and_libraries import roadsAndLibraries

def test_roadAndLibraries():
    test_num_cities_1 = 3
    test_lib_cost_1 = 2
    test_road_cost_1 = 1
    test_cities_1 = [[1, 2], [3, 1], [2, 3]]
    
    test_num_cities_2 = 6
    test_lib_cost_2 = 2
    test_road_cost_2 = 5
    test_cities_2 = [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]
    
    assert roadsAndLibraries(test_num_cities_1, test_lib_cost_1, test_road_cost_1, test_cities_1) == 4
    assert roadsAndLibraries(test_num_cities_2, test_lib_cost_2, test_road_cost_2, test_cities_2) == 12