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

const breadthFirstPrint = (graph, source) => {
    const queue = [ source ];

    while (queue.length > 0){
        const current = queue.shift();
        console.log("current:", current);
        
        for (let neighbor of graph[current])
            queue.push(neighbor);
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

breadthFirstPrint(graph, 'a'); // a, b, c, d, e, f

// NOTE: Breadth first traversal can only be implemented iteratively using a Queue.
// This is because if we try to implement it using recursion, underlying it will use a stack.
// The Queue and the stack would be fighting over the order to traverse.