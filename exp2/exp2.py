

graph = {
    'A': ['B'],
    'B': ['D', 'E'],
    'D': [],
    'E': ['F'],
    'F': []
}
def dfs(graph, current, target, path):
    path.append(current)
    if current == target:
        return True
    for neighbour in graph[current]:
        if dfs(graph, neighbour, target, path):
            return True
    path.pop()
    return False
path = []
if dfs(graph, 'A', 'F', path):
    print("Path:", ' -> '.join(path))
else:
    print("Path not found")
