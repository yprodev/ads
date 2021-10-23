// Undirected graph
const edges = [
	['i', 'j'],
	['k', 'i'],
	['m', 'k'],
	['k', 'l'],
	['o', 'n']
];


// Undirected cyclic graph
const graph = {
	// ['i', 'j'],
	// i: [],
	// j: []
	i: ['j', 'k'],
	j: ['i'],
	k: ['i', 'm', 'l'],
	m: ['k'],
	l: ['k'],
	o: ['n'],
	n: ['o']
};


const undirectedPath = (edges, nodeA, nodeB) => {
	const graph = buildGraph(edges);

	return hasPath(graph, nodeA, nodeB, new Set());
};

// Graph traversal
const hasPath = (graph, src, dst, visited) => {
	if (src === dst) return true;
	if (visited.has(src)) return false;

	visited.add(src);

	for (let neighbor of graph[src]) {
		if (hasPath(graph, neighbor, dst, visited) === true) {
			return true;
		}
	}

	return false;
};

// Convert edge list into adjacency list
const buildGraph = (edges) => {
	const graph = {};

	for (let edge of edges) {
		const [ a, b ] = edge;

		if (!(a in graph)) graph[a] = [];
		if (!(b in graph)) graph[b] = [];

		graph[a].push(b);
		graph[b].push(a);
	}

	return graph;
};


console.log(undirectedPath(edges, 'j', 'm'));