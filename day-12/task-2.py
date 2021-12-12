def get_paths(vertex, allowed_twice, path):
    path += vertex
    if vertex == 'end':
        paths.add(path)
        return
    if vertex.islower():
        if vertex == allowed_twice:
            allowed_twice = ''
        else:
            graph.get(vertex)[0] = True

    for neighbour in graph.get(vertex)[1]:
        if not graph.get(neighbour)[0]:
            get_paths(neighbour, allowed_twice, path)

    graph.get(vertex)[0] = False


with open("input.txt") as f:
    edges = [line.strip().split('-') for line in f.readlines()]

graph = {}
for edge in edges:
    if edge[0] not in graph:
        graph.update({edge[0]: [False, []]})
    if edge[1] not in graph:
        graph.update({edge[1]: [False, []]})
    graph.get(edge[0])[1].append(edge[1])
    graph.get(edge[1])[1].append(edge[0])

paths = set()
for vertex in graph.keys():
    if vertex.islower() and vertex != 'start':
        get_paths('start', vertex, '')
print(len(paths))
