class UnionFind:
    def __init__(self, n):
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [0] * n
        self.size: list[int] = [1] * n
        self.max_size: int = 1
    
    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u: int, v: int) -> None:
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
                self.max_size = max(self.max_size, self.size[root_u])
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
                self.max_size = max(self.max_size, self.size[root_v])
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
                self.size[root_u] += self.size[root_v]
                self.max_size = max(self.max_size, self.size[root_u])

def maxCircle(queries):
    people_map = {}
    next_id = 0
    max_circle_sizes = []
    
    for a, b in queries:
        if a not in people_map:
            people_map[a] = next_id
            next_id += 1
        if b not in people_map:
            people_map[b] = next_id
            next_id += 1
    
    uf = UnionFind(next_id) # type: ignore
    
    for a, b in queries:
        uf.union(people_map[a], people_map[b])
        max_circle_sizes.append(uf.max_size)
    
    return max_circle_sizes
            