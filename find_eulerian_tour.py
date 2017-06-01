# 04.05.2017


def find_eulerian_tour(graph):
    # your code here
    result = []
    first, second = graph[0]
    result.append(first)
    result.append(second)
    graph.pop(0)
    currentNode = result[-1]

    while graph:
        for tup in graph:
            if currentNode in tup:
                index = graph.index(tup)
                result.append(tup[tup.index(currentNode) - 1])
                graph.pop(index)
                currentNode = result[-1]

    return result


print(find_eulerian_tour([(8, 16), (8, 18), (16, 17), (18, 19),
                          (3, 17), (13, 17), (5, 13), (3, 4), (0, 18), (3, 14),
                          (11, 14), (1, 8), (1, 9), (4, 12), (2, 19), (1, 10),
                          (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18),
                          (5, 6), (7, 15), (8, 13), (10, 17)]))
