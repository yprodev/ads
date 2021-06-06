function hastStringToInt(string, tableSize) {
	let hash = 17;

	for (let i = 0; i < string.length; i++) {
		hash = (13 * hash * string.charCodeAt(i)) % tableSize;
	}

	return hash;
}

class HashTable {
	table = new Array(3);

	setItem = (key, value) => {
		const index = hastStringToInt(key, this.table.length);

		if (this.table[index]) {
			this.table[index].push([key, value]);
		} else {
			this.table[index] = [[key, value]];
		}

	}

	getItem = (key) => {
		const index = hastStringToInt(key, this.table.length);

		if (!this.table[index]) {
			return null;
		}

		return this.table[index].find(x => x[0] === key)[1];
	};
}

const myTable = new HashTable();
myTable.setItem('firstName', 'bob');
myTable.setItem('lastName', 'tim');
myTable.setItem('age', 5);
myTable.setItem('dob', '1/2/3');
console.log(myTable.getItem('firstName'));
console.log(myTable.getItem('lastName'));
console.log(myTable.getItem('age'));
console.log(myTable.getItem('dob'));








