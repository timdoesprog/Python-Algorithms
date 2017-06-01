# 04.05.2017
# create an eulerian tour from given nodes


def create_tour(nodes):
    result = []
    for i in range(len(nodes)):
        if i == len(nodes) - 1:
            result.append((nodes[i], nodes[0]))
            break
        result.append((nodes[i], nodes[i + 1]))
    return result


print(create_tour([1, 2, 3]))
