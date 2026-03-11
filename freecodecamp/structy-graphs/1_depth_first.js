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

const depthFirstPrint = (graph, source) => {
    const stack = [ source ];

    while (stack.length > 0){
        const current = stack.pop();
        console.log("current:", current)

        for (let neighbor of graph[current]){
            stack.push(neighbor);
        } 
    }

};

const graph = {
  a: ['b', 'c'],
  b: ['d'],
  c: ['e'],
  d: ['f'],
  e: [],
  f: []
};

depthFirstPrint(graph, 'a'); // a, c, e, b, d, f