# Graph structure
#
# a
# ├── b
# │   └── d
# │       └── f
# └── c
#     └── e
#
# Edges:
# a -> b, c
# b -> d
# c -> e
# d -> f

from collections import deque

def breadth_first_print(graph, source):
    queue = deque()
    queue.append(source)

    while queue:
        current = queue.popleft()
        print("current:", current)
        for n in graph[current]:
            queue.append(n)

graph = {
  "a": ["b", "c"],
  "b": ["d"],
  "c": ["e"],
  "d": ["f"],
  "e": [],
  "f": []
}

breadth_first_print(graph, "a"); # a, b, c, d, e, f