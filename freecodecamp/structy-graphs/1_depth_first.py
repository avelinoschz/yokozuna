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

def depth_first_print(graph, source):
    stack = []
    stack.append(source)

    while stack:
        current = stack.pop()
        print("current:", current)

        for n in graph[current]:
            stack.append(n)


graph = {
  "a": ["b", "c"],
  "b": ["d"],
  "c": ["e"],
  "d": ["f"],
  "e": [],
  "f": []
}

depth_first_print(graph, "a"); # a, c, e, b, d, f