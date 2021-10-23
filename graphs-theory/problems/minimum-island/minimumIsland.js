const grid = [
	['W', 'L', 'W', 'W', 'W'],
	['W', 'L', 'W', 'W', 'W'],
	['W', 'W', 'W', 'L', 'W'],
	['W', 'W', 'L', 'L', 'W'],
	['L', 'W', 'W', 'L', 'L'],
	['L', 'L', 'W', 'W', 'W']
]; // -> 2

const minimumIsland = (grid) => {
	const visited = new Set();
	let minSize = Infinity;

	for (let row = 0; row < grid.length; row++) {
		for (let col = 0; col < grid[0].length; col++) {
			const size = exploreSize(grid, row, col, visited);
			if (size > 0 && size < minSize) {
				minSize = size;
			}
		}
	}

	return minSize;
};

const exploreSize = (grid, row, col, visited) => {
	const rowInbounds = row >= 0 && row < grid.length;
	const colInbounds = col >= 0 && col < grid[0].length;

	if (!rowInbounds || !colInbounds) return 0;

	if (grid[row][col] === 'W') return 0;

	const pos = row + ',' + col;

	if (visited.has(pos)) return 0;

	visited.add(pos);

	let size = 1;

	size += exploreSize(grid, row - 1, col, visited);
	size += exploreSize(grid, row + 1, col, visited);
	size += exploreSize(grid, row, col - 1, visited);
	size += exploreSize(grid, row, col + 1, visited);

	return size;
};

console.log('result: ', minimumIsland(grid));
