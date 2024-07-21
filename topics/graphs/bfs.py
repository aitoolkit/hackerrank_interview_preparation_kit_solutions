from typing import Any

class Graph():
    def __init__(self, n):
        self.adj_list: list[list[Any]] = [[] for _ in range(n)]
        self.n = n
        
    def connect(self, x, y):
        self.adj_list[x].append(y)
        self.adj_list[y].append(x)
    
    def find_all_distances(self, v):
        distances = [-1] * self.n
        distances[v] = 0
        queue =[v]
        
        while queue:
            current = queue.pop(0)
            for neighbor in self.adj_list[current]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current] + 6
                    queue.append(neighbor)
        result = [distances[i] for i in range(self.n) if i != v]
        print(*result)
        return result


# t = int(input())
# for i in range(t):
#     n,m = [int(value) for value in input().split()]
#     graph = Graph(n)
#     for i in range(m):
#         x,y = [int(x) for x in input().split()]
#         graph.connect(x-1,y-1) 
#     s = int(input())
#     graph.find_all_distances(s-1)