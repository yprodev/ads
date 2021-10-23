const grid = [
	['W', 'L', 'W', 'W', 'W'],
	['W', 'L', 'W', 'W', 'W'],
	['W', 'W', 'W', 'L', 'W'],
	['W', 'W', 'L', 'L', 'W'],
	['L', 'W', 'W', 'L', 'L'],
	['L', 'L', 'W', 'W', 'W']
]; // -> 3

const islandCount = (grid) => {
	const visited = new Set();
	let count = 0;
	for (let r = 0; r < grid.length; r++) {
		for (let c = 0; c < grid[0].length; c++) {
			if (explore(grid, r, c, visited) === true) {
				count += 1;
			}
		}
	}

	return count;
};

const explore = (grid, row, col, visited) => {
	const rowInbounds = 0 <= row && row < grid.length;
	const colInbounds = 0 <= col && col < grid.length;

	if (!rowInbounds || !colInbounds) return false;

	if (grid[row][col] === 'W') return false;

	const pos = row + ',' + col;

	if (visited.has(pos)) return false;

	visited.add(pos);

	explore(grid, row - 1, col, visited);
	explore(grid, row + 1, col, visited);
	explore(grid, row, col - 1, visited);
	explore(grid, row, col + 1, visited);

	return true;
};

console.log('result: ', islandCount(grid));
