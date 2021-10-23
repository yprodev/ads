const depthFirstPrint = (graph, source) => {
	const stack = [ source ];

	while (stack.length > 0) {
		const current = stack.pop();

		console.log('cur:', current)

		for (let neighbor of graph[current]) {
			stack.push(neighbor);
		}
	}
};

const graph = {
	a: ['c', 'b'],
	b: ['d'],
	c: ['e'],
	d: ['f'],
	e: [],
	f: []
};

depthFirstPrint(graph, 'a'); // abdfce