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
    current = source
    print("current:", current)

    for n in graph[current]:
        depth_first_print(graph, n)


graph = {
  "a": ["b", "c"],
  "b": ["d"],
  "c": ["e"],
  "d": ["f"],
  "e": [],
  "f": []
}

depth_first_print(graph, "a"); # a, c, e, b, d, f