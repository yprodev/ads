class Node {
	constructor(val) {
		this.value = val;
		this.left = null;
		this.right = null;
	}
}

const a = new Node(5);
const b = new Node(11);
const c = new Node(3);
const d = new Node(3);
const e = new Node(15);
const f = new Node(12);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;


module.exports = { binaryNumberWithMinTree: a };

/*
        a
       / \
      b   c
     / \   \
    d   e   f
*/