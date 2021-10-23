// Acyclic & directed graph
const graph = {
	f: ['g', 'i'],
	g: ['h'],
	h: [],
	i: ['g', 'k'],
	j: ['i'],
	k: []
};

// We need source and destination nodes to find a path
const hasPath = (graph, src, dst) => {
	if (src === dst) return true;

	for (let neighbor of graph[src]) {
		if (hasPath(graph, neighbor, dst) === true) {
			return true;
		}
	}

	return false;
};

console.log(hasPath(graph, 'f', 'k'));


