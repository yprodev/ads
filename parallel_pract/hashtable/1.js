function hastStringToInt(string, tableSize) {
	let hash = 17;

	for (let i = 0; i < string.length; i++) {
		hash = (13 * hash * string.charCodeAt(i)) % tableSize;
	}

	return hash;
}

class HashTable {
	table = new Array(3);
	numItems = 0;

	resize = () => {
		const newTable = new Array(this.table.length * 2);

		for (let i = 0; i < this.table.length; i++) {
			if (this.table[i]) {
				this.table[i].forEach(([key, value]) => {
					const index = hastStringToInt(key, newTable.length);

					if (newTable[index]) {
						newTable[index].push([key, value]);
					} else {
						newTable[index] = [[key, value]];
					}

				});
			}
		}

		this.table = newTable;
	}

	setItem = (key, value) => {
		this.numItems++;

		const loadFactor = this.numItems / this.table.length;

		if (loadFactor > .8) {
			this.resize();
		}

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
console.log(myTable.table.length);
myTable.setItem('lastName', 'tim');
myTable.setItem('age', 5);
myTable.setItem('dob', '1/2/3');
console.log(myTable.table.length);
console.log(myTable.getItem('firstName'));
console.log(myTable.getItem('lastName'));
console.log(myTable.getItem('age'));
console.log(myTable.getItem('dob'));








