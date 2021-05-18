import time
import math
from graphviz import Digraph


def evaluate(graph, path):
    cost = 0
    for i in range(len(path)):
        first = path[i]
        second = path[i + 1] if i < len(path) - 1 else path[0]
        cost += graph[first][second]
    return cost


def tsp_bfs(graph):
    n = len(graph)
    queue = []

    def expand(path):
        for i in range(n):
            if i not in path:
                new_path = path.copy()
                new_path.append(i)
                queue.append(new_path)

    best = float("inf")
    expand([])
    while len(queue) > 0:
        path = queue.pop()
        if len(path) == n:
            cost = evaluate(graph, path)
            if cost < best:
                best = cost
        else:
            expand(path)
    return best


def tsp_dfs(graph, path=[]):
    n = len(graph)
    if len(path) == n:
        return evaluate(graph, path)
    best = float("inf")
    for i in range(n):
        if i not in path:
            new_path = path.copy()
            new_path.append(i)
            cost = tsp_dfs(graph, new_path)
            if cost < best:
                best = cost
    return best


best = float("inf")


def tsp_backtracking(graph):
    n = len(graph)

    def visit(path):
        global best
        cost = evaluate(graph, path)
        if cost > best:
            return
        if len(path) == n:
            if cost < best:
                best = cost
            return
        for i in range(n):
            if i not in path:
                new_path = path.copy()
                new_path.append(i)
                visit(new_path)

    visit([])
    return best


def time_function(graph, func):
    starting_time = time.process_time()
    result = func(graph)
    ending_time = time.process_time()
    elapsing_time = ending_time - starting_time
    print(
        f"The method {func.__name__} took {elapsing_time} seconds and got the value {result}"
    )


# Prishtine
# Mitrovice
# Gjilan
# Ferizaj
# Prizren
# Gjakove

graph = [
[0,41,48,42,85,88],
[41,0,84,74,104,84],
[48,84,0,34,124,127],
[42,74,34,0,64,88],
[85,104,124,64,0,40],
[88,84,127,88,40,0]
]

def render_graph():
    cities =['Prishtine','Mitrovice','Gjilan','Ferizaj','Prizren','Gjakove']
    labels = ['A','B','C','D','E','F']
    dot = Digraph(comment='Qytetet e kosoves')

    for i in range(len(cities)):
        dot.node(labels[i],cities[i])

    edges = []
    for label in labels:
        for l in labels:
            if l == label:
                continue
            if f'{l}{label}' in edges:
                continue
            edges.append(f'{label}{l}')
    dot.edges(edges)

    dot.render('./round-table.gv', view=True)



time_function(graph, tsp_bfs)
time.sleep(1)
time_function(graph, tsp_dfs)
time.sleep(1)
time_function(graph, tsp_backtracking)
render_graph()
