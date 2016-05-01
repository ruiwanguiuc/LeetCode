def topo_sort(nodes, edges):
    def dfs(v):
        visited.add(v)
        visited_this_call.add(v)
        if v in edges:
            for n in edges[v]:
                if n in visited_this_call:
                    return False
                if n not in visited:
                    if not dfs(n):
                        return False
        order.append(v)
        visited_this_call.remove(v)
        return True

    order = []
    visited = set()
    for v in nodes:
        if v not in visited:
            visited_this_call = set()
            if not dfs(v):
                return []
    return list(reversed(order))

if __name__ == "__main__":
    edges = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
    }
    nodes = ['b', 'a', 'c', 'd']
    print(topo_sort(nodes, edges))

    # there is a cycle, should return []
    edges = {
        'a': ['b'],
        'b': ['a'],
    }
    nodes = ['a', 'b']
    print(topo_sort(nodes, edges))

    # there is a cycle, should return []
    edges = {
        'a': ['b', 'd'],
        'b': ['c'],
        'c': ['a'],
    }
    nodes = ['a', 'b', 'c', 'd']
    print(topo_sort(nodes, edges))
