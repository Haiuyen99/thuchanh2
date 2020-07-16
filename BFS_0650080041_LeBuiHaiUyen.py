map = {
    "Arad": {"Sibiu": 140, "Timisoara": 118, "Zerind": 75},
    "Timisoara": {"Lugoj": 111, "Arad": 118},
    "Lugoj": {"Mehadia": 70, "Timisoara": 111},
    "Mehadia": {"Dobreta": 75, "Lugoj": 70},
    "Dobreta": {"Craiova": 120, "Mehadia": 75},
    "Craiova": {"Rimnicu Vilcea": 146, "Pitesti": 138, "Dobreta": 120},
    "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146},
    "Sibiu": {"Arad": 140, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Zerind": {"Oradea": 71, "Arad": 75},
    "Oradea": {"Sibiu": 151, "Zerind": 71},
    "Fagaras": {"Bucharest": 211, "Sibiu": 99},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Bucharest": {"Giurgui": 90, "Fagaras": 211, "Pitesti": 101, "Urziceni": 85},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "lasi": 92},
    "lasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"lasi": 87},
    "Giurgui": {"Bucharest": 90}

}


def dfs(map, start):
    if not start in map.keys():
        return None
    stack = []
    path = []
    visited = []
    for n in map[start]:
        stack.append(n)
    path.append(start)
    visited.append(start)
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited: path.append(node)
        for n in map[node]:
            if n not in visited:
                stack.append(n)
        visited.append(node)
    return path


b = dfs(map, 'Arad')
print("Đường đi đến đích là : {}".format(b))