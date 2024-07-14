from typing import Any


def dfs(city: int, visited: list[Any], graph: list[Any]) -> None:
    stack = [city]
    visited[city] = True
    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        # If the cost of a library is less than or equal to the cost of a road, build a library in each city
        return n * c_lib
    
    # Create an adjacency list for the graph
    graph: list[Any] = [[] for _ in range(n + 1)]
    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    connected_components = 0
    
    for city in range(1, n + 1):
        if not visited[city]:
            dfs(city, visited, graph)
            connected_components += 1

    # For each connected component, we need one library and (size_of_component - 1) roads
    # Total cost = (number of components) * c_lib + (total number of cities - number of components) * c_road
    total_cost = connected_components * c_lib + (n - connected_components) * c_road
    return total_cost

# list1 = [1]
# list2 = list1
# list2.append(2)
# print(list1, list2) # [1, 2] [1, 2]