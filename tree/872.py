

# ===================================================================================

# [AUTHOR]: lee215
# [DESCRIPTION]: [C++/Java/Python] O(H) Space

def leafSimilar(self, root1, root2):
    def dfs(node):
        if not node: return
        if not node.left and not node.right: yield node.val
        for i in dfs(node.left): yield i
        for i in dfs(node.right): yield i
    return all(a == b for a, b in itertools.izip_longest(dfs(root1), dfs(root2)))

# ===================================================================================

# [AUTHOR]: HeroKillerEver
# [DESCRIPTION]: 4 line Python Solution

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.findleaf(root1) == self.findleaf(root2)
        
    def findleaf(self, root):
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.findleaf(root.left) + self.findleaf(root.right)


# ===================================================================================

# [AUTHOR]: ttsugrii
# [DESCRIPTION]: 0ms parallel iterative in-order traversals in C++

"""
The idea is to perform iterative in-order traversals for both trees at the same time and report mismatch as soon as some pair of leaves do not have the same value. In case no mismatch is found and both trees are fully explored - both trees are leaf-similar.

class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        if (root1 == root2) return true;
        if (root1 == nullptr || root2 == nullptr) return false;
        stack<TreeNode*> s1; s1.push(root1);
        stack<TreeNode*> s2; s2.push(root2);
        while (!s1.empty() && !s2.empty()) {
            auto node1 = s1.top(); s1.pop();
            while (node1->left || node1->right) {
                if (node1->left) {
                    if (node1->right) s1.push(node1->right);
                    node1 = node1->left;
                } else {
                    node1 = node1->right;
                }
            }
            auto node2 = s2.top(); s2.pop();
            while (node2->left || node2->right) {
                if (node2->left) {
                    if (node2->right) s2.push(node2->right);
                    node2 = node2->left;
                } else {
                    node2 = node2->right;
                }
            }
            if (node1->val != node2->val) return false;
        }
        return s1.empty() && s2.empty();
    }
};


"""

# ===================================================================================

# [AUTHOR]: dipesh1502
# [DESCRIPTION]: Python beats 100% ( 36 ms Iterative )

def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.iterative(root1,[]) == self.iterative(root2,[])
        
    def iterative(self,root,s):
        if root is not None:
            stack = []
            stack.append(root)
            while stack:
                x = stack.pop(-1)
                if x.left is None and x.right is None:
                    s.append(x.val)
                    continue
                if x.right is not None:
                    stack.append(x.right)
                if x.left is not None:
                    stack.append(x.left)
        return s

"""
Comment Area:
# [AUTHOR]: Talse

"""

# IV). Get Leaf Sequence -- Iteration
# | O(T): O(n) | O(S): O(n) | Rt: 28ms |

def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    def getLeaf(node):
        rst, s = [], [(node, 0)]
        while s:
            node, visited = s.pop()
            if not node: continue
            if not visited: 
                s.extend([(node.right, 0), (node, 1), (node.left, 0)])
            else:
                if not node.left and not node.right: rst.append(node.val)
        return rst
    return getLeaf(root1) == getLeaf(root2)


# V). Get Leaf Sequence -- Stack
# | O(T): O(n) | O(S): O(n) | Rt: 24ms |

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeaf(node):
            rst, stack = [], []
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                if not node.right and not node.left: rst.append(node.val)
                node = node.right
            return rst
        return getLeaf(root1) == getLeaf(root2)


# ===================================================================================

# [AUTHOR] ME
# [DESCRIPTION] First working solution
# Issues:
#	

# Recursion solution
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafs1, leafs2 = [], []
        
        def recur(root, leafList):
            if root is None:
                return
            
            recur(root.left, leafList)
            recur(root.right, leafList)
            
            if root.left is None and root.right is None:
                leafList.append(root.val)

        recur(root1, leafs1)
        recur(root2, leafs2)
        
        
        return leafs1 == leafs2

# Implement iterative version