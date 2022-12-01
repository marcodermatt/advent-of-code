def get_paths(vertex):
    if vertex == 'end':
        return 1
    if vertex.islower():
        graph.get(vertex)[0] = True
    count = 0
    for neighbour in graph.get(vertex)[1]:
        if not graph.get(neighbour)[0]:
            count += get_paths(neighbour)
    graph.get(vertex)[0] = False
    return count


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

print(get_paths('start'))
