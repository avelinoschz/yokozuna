// Graph structure

// a
// ├── b
// │   └── d
// │       └── f
// └── c
//     └── e

// Edges:
// a -> b, c
// b -> d
// c -> e
// d -> f

const depthFirstPrint = (graph, source) =>  {
    console.log("current:", source)

    for (let neighbor of graph[source]){
        depthFirstPrint(graph, neighbor)
    }
}

const graph = {
  a: ['b', 'c'],
  b: ['d'],
  c: ['e'],
  d: ['f'],
  e: [],
  f: []
};

depthFirstPrint(graph, 'a'); // a, b, d, f, c, e