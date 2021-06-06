# [AUTHOR]: groothedde
# [DESCRIPTION]: C++ 97.97% without a massive array or using a map, BST

"""
// https://www.geeksforgeeks.org/fast-io-for-competitive-programming/
// https://codeforces.com/blog/entry/10297
// People are not actually implementing any form of hash set, so I use tricks
static const int _ = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}();

struct MyHashSetNode {
    int val;
    MyHashSetNode *left, *right;
    
    MyHashSetNode(int v) : val(v), left(nullptr), right(nullptr) {}
    ~MyHashSetNode() {
        if(left  != nullptr) delete left;
        if(right != nullptr) delete right;
    }
};

class MyHashSetTree {
private:
    MyHashSetNode *root;
public:
    MyHashSetTree() : root(nullptr) {}
    ~MyHashSetTree() {
        if(root != nullptr) 
            delete root; // traverses through destructors
    }
    
    MyHashSetNode *Insert(int x, MyHashSetNode *parent) {
        MyHashSetNode *result = parent;

        if (parent == nullptr) {
            result = new MyHashSetNode(x);
        } else if (x < parent->val) {
            parent->left = Insert(x, parent->left);
        } else if (x > parent->val) {
            parent->right = Insert(x, parent->right);
        } else {
            return nullptr; // duplicate, add should not comply
        }

        return result;
    }
    
    bool Insert(int x) {
        if(Find(x) != nullptr)
            return false;
        
        root = Insert(x, root);
        return true;
    }
    
    MyHashSetNode *Find(int x, MyHashSetNode *parent) {
        MyHashSetNode *current = parent;
        int currentValue;

        while (current != nullptr) {
            currentValue = current->val;
            if (x < currentValue) {
                current = current->left;
            } else if (x > currentValue) {
                current = current->right;
            } else {
                return current;
            }
        }

        return nullptr;
    }
    
    MyHashSetNode *Find(int x) {
        if (root != nullptr) 
            return Find(x, root);

        return nullptr;
    }
    
    MyHashSetNode *FindMin(MyHashSetNode *parent) {
        MyHashSetNode *current = parent;
        MyHashSetNode *left = nullptr;

        if (current != nullptr) {
            while ((left = current->left) != nullptr)
                current = left;
        }

        return current;
    }

    MyHashSetNode *RemoveMin(MyHashSetNode *parent) {
        if (parent == nullptr) {
            return nullptr;
        } else if (parent->left != nullptr) {
            parent->left = RemoveMin(parent->left);
            return parent;
        } else {
            MyHashSetNode *result = parent->right;

            parent->right = parent->left = nullptr;
            delete parent;
            return result;
        }
    }
    
    MyHashSetNode *Remove(int x, MyHashSetNode *parent) {
        MyHashSetNode *current = parent;
        MyHashSetNode *left = nullptr;
        MyHashSetNode *right = nullptr;
        int currentValue;

        if (current != nullptr) {
            left = current->left;
            right = current->right;
            currentValue = current->val;
        }

        if (current == nullptr) {
            return nullptr;
        } else if (x < currentValue) {
            current->left = Remove(x, left);
        } else if (x > currentValue) {
            current->right = Remove(x, right);
        } else if (left != nullptr && right != nullptr) {
            current->val = FindMin(right)->val;
            current->right = RemoveMin(right);
        } else {
            current = (left != nullptr) ? left : right;

            parent->right = parent->left = nullptr;
            delete parent;
        }

        return current;
    }
    
    bool Remove(int x) {
        if(Find(x) == nullptr)
            return false;
        
        root = Remove(x, root);
        return true;
    }
};

class MyHashSet {
private:
    MyHashSetTree tree;
public:
    /** Initialize your data structure here. */
    MyHashSet() {
        
    }
    
    void add(int key) {
        tree.Insert(key);
    }
    
    void remove(int key) {
        tree.Remove(key);
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return tree.Find(key) != nullptr;
    }
};

"""


# ===================================================

# [AUTHOR]: emwalker
# [DESCRIPTION]: Python hash set with trivial hash function

class MyHashSet:
    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)

    def remove(self, key):
        bucket, idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)

    def contains(self, key):
        _, idx = self._index(key)
        return idx >= 0

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1

# ===================================================

# [AUTHOR]: rainingpeace
# [DESCRIPTION]: (C++) 705. Design HashSet


"""
class MyHashSet {
private: 
    vector<bool> data; 
    
public:
    /** Initialize your data structure here. */
    MyHashSet() {
        data = vector<bool>(1000001, false);
    }
    
    void add(int key) {
        data[key] = true; 
    }
    
    void remove(int key) {
        data[key] = false; 
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return data[key]; 
    }
};

"""

# ===================================================

# [AUTHOR]: alifov
# [DESCRIPTION]: EASY, SIMPLE, CLEAN. Using an array and (modulo) hashing

"""

/**
 * Initialize your data structure here.
 */
var MyHashSet = function() {
    this.array = new Array(100000).fill(null);    
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function(key) {
    this.array[this.getHashCode(key)] = key;
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function(key) {
    this.array[this.getHashCode(key)] = null;
};

/**
 * Returns true if this set contains the specified element 
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function(key) {
    return this.array[this.getHashCode(key)] !== null;
};

MyHashSet.prototype.getHashCode = function(key) {
    return key % 99999;
};
"""

# ===================================================

# [AUTHOR]: DBabichev
# [DESCRIPTION]: [Python] Easy Multiplicative Hash, explained


"""
The goal of this problem is to create simple hash function, not using build-in methods. One of the simplest, but classical hashes are so-called Multiplicative hashing: https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing.
The idea is to have hash function in the following form.
image

Here we use the following notations:

K is our number (key), we want to hash.
a is some big odd number (sometimes good idea to use prime number) I choose a = 1031237 without any special reason, it is just random odd number.
m is length in bits of output we wan to have. We are given, that we have no more than 10000 operations overall, so we can choose such m, so that 2^m > 10000. I chose m = 15, so in this case we have less collistions.
if you go to wikipedia, you can read that w is size of machine word. Here we do not really matter, what is this size, we can choose any w > m. I chose m = 20.
So, everything is ready for function eval_hash(key): ((key*1031237) & (1<<20) - 1)>>5. Here I also used trick for fast bit operation modulo 2^t: for any s: s % (2^t) = s & (1<<t) - 1.

How our HashSet will look and work like:

We create list of empty lists self.arr = [[] for _ in range(1<<15)].
If we want to add(key), then we evaluate hash of this key and then add this key to the place self.arr[t]. However first we need to check if this element not it the list. Ideally, if we do not have collisions, length of all self.arr[i] will be 1.
If we want to remove(key) element, we first evaluate it hash, check corresponding list, and if we found element in this list, we remove it from this list.
Similar with contains(key), just check if it is in list.
Complexity: easy question is about space complexity: it is O(2^15), because this is the size of our list. We have a lot of empty places in this list, but we still need memory to allocate this list of lists. Time complexity is a bit tricky. If we assume, that probability of collision is small, than it will be in average O(1). However it really depends on the size of our self.arr. If it is very big, probability is very small. If it is quite tight, it will increase. For example if we choose size 1000000, there will be no collisions at all, but you need a lot of memory. So, there will always be trade-off between memory and time complexity.
"""

class MyHashSet: 
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]

# ===================================================

# [AUTHOR]: rosemelon
# [DESCRIPTION]: Python Chaining

"""
I could write a 4-line solution, but I want to make sure I can write a well-thought out solution if I ever get asked this question in an interview. The question is trivial if we only have 10,000 possible values in our set, but if you're at Google and they process billions of web pages, you might run out of memory in your Hashset if you just use an array.

Implementation: Create buckets with an array, each bucket has a linked list so you can delete and add in O(1) time. O(N) time for search.

Improvement: I should add load factor rehashing in order to rehash if LF is above 3/4. Possible tradeoffs with red black tree instead of linked list. Add/delete/search is O(log N) for a red-black tree. If you are searching very rarely, it might be better to go with the linked list, otherwise maybe real world applications would do better with the tree? Not sure, but it might be worth mentioning in an interview.

It might be more helpful for LeetCode to limit the amount of buckets in the array so people don't pass the test case without thinking through the point of the problem. There is no point in doing problems just to get a green checkmark -- you should do problems to understand them so you can do well in the interview.

Awesome answer in Java: https://leetcode.com/problems/design-hashset/discuss/249424/A-complete-Java-Solution-using-load-factor-BST-Rehashing!-Faster-than-90
"""

class ListNode(object):
    def __init__(self,key,next):
        self.key = key
        self.next = next

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [None]*self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketCode = key % self.size
        cur = self.buckets[bucketCode]
        if not cur: 
            self.buckets[bucketCode] = ListNode(key, None)
            return
        if cur.key == key:
            return 
        while cur:
            if cur.key == key: 
                return
            if not cur.next: 
                cur.next = ListNode(key,None)
                return 
            if cur.next: 
                cur = cur.next
        return 

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketCode = key % self.size
        cur = self.buckets[bucketCode]
        if not cur:
            return 
        if cur.key == key:
            self.buckets[bucketCode] = cur.next
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return 
            cur = cur.next
        return
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketCode = key % self.size
        cur = self.buckets[bucketCode]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False


# ===================================================


# [AUTHOR] ME
# [DESCRIPTION] First NOT working solution
# Issues:
#	list index is out of range for remove method with self.items.pop(index)
#	Fails on big test case: Time Limit Exceeded

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []

    def __len__(self):
        return len(self.items)
        
        
    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        return self.items.append(key)
        

    def remove(self, key: int) -> None:      
        if not self.contains(key):
            return

        for i in range(len(self)):
            if key in self.items:                
                self.items.remove(key)
            
            
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if (self.isEmpty()):
            return False
        
        for i in range(len(self)):
            if key in self.items:
                return True
            
            return False
        
        
        
    def isEmpty(self):
        if len(self) == 0:
            return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# [AUTHOR] ME (copied version from emwalker)
# [DESCRIPTION] First working solution

class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)

    def remove(self, key: int) -> None:
        bucket, idx = self._index(key)
        if idx < 0: # Here was non-obvious error when you put 'idx <= 0' instead of 'idx < 0'
            return
        bucket.remove(key)

    def contains(self, key: int) -> bool:
        bck, idx = self._index(key)
        return idx >= 0

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]

        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i

        return bucket, -1
