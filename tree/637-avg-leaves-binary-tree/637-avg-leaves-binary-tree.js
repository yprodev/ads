// [AUTHOR]: sgallivan
// [DESCRIPTION]: JS, Python, Java, C++ | Easy BFS Solution w/ Explanation

/*

(Note: This is part of a series of Leetcode solution explanations. If you like this solution or find it useful, please upvote this post.)

Idea:
A problem talking about levels in a binary tree should immediately bring to mind a breadth-first search (BFS) approach. The classic BFS approach for a binary tree is to use a queue and push each queue entry's children onto the end of the queue. This way, the queue will run to the end of the row/level before moving onto the next level.

When a problem requires you to isolate a level, you can simply take the length of the queue at the start of the row and then once you've processed that many nodes from the queue, you'll know that you're ready to start the next row.

So as long as the queue exists, we'll take each row, sum the row's values (row), then divide by the length of the row (qlen) to find the average, pushing each average into our answer array (ans).

Implementation:
The code for all four languages is almost identical.


*/

var averageOfLevels = function(root) {
    let q = [root], ans = []
    while (q.length) {
        let qlen = q.length, row = 0
        for (let i = 0; i < qlen; i++) {
            let curr = q.shift()
            row += curr.val
            if (curr.left) q.push(curr.left)
            if (curr.right) q.push(curr.right)
        }
        ans.push(row/qlen)
    }
    return ans
};

/*

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q, ans = [root], []
        while len(q):
            qlen, row = len(q), 0
            for i in range(qlen):
                curr = q.pop(0)
                row += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            ans.append(row/qlen)
        return ans


class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>(List.of(root));
        List<Double> ans = new ArrayList<>();
        while (q.size() > 0) {
            double qlen = q.size(), row = 0;
            for (int i = 0; i < qlen; i++) {
                TreeNode curr = q.poll();
                row += curr.val;
                if (curr.left != null) q.offer(curr.left);
                if (curr.right != null) q.offer(curr.right);
            }
            ans.add(row/qlen);
        }
        return ans;
    }
}


class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        vector<double> ans;
        while (q.size()) {
            double qlen = q.size(), row = 0;
            for (int i = 0; i < qlen; i++) {
                TreeNode* curr = q.front(); q.pop();
                row += curr->val;
                if (curr->left) q.push(curr->left);
                if (curr->right) q.push(curr->right);
            }
            ans.push_back(row/qlen);
        }
        return ans;
    }
};



*/

// ===================================================


// [AUTHOR]: earlme
// [DESCRIPTION]: Java BFS Solution

/*

Classic bfs problem. At each level, compute the average since you already know the size of the level.

public List<Double> averageOfLevels(TreeNode root) {
    List<Double> result = new ArrayList<>();
    Queue<TreeNode> q = new LinkedList<>();
    
    if(root == null) return result;
    q.add(root);
    while(!q.isEmpty()) {
        int n = q.size();
        double sum = 0.0;
        for(int i = 0; i < n; i++) {
            TreeNode node = q.poll();
            sum += node.val;
            if(node.left != null) q.offer(node.left);
            if(node.right != null) q.offer(node.right);
        }
        result.add(sum / n);
    }
    return result;
}

*/

// ===================================================


// [AUTHOR]: thoai_huynh
// [DESCRIPTION]: BFS Javascript


var averageOfLevels = function(root) {
    const queue = [root]
    const result = []
    
    while (queue.length > 0) {
        const size = queue.length
        let sum = 0
        
        for (let i = 0;i < size;i++) {
            const node = queue.shift()
            
            if (node) {
                sum += (node.val || 0)
                node.left && queue.push(node.left)
                node.right && queue.push(node.right)
            }
        }
        
        result.push((sum / size))
    }
    return result
};

// ===================================================


// [AUTHOR]: shengdade
// [DESCRIPTION]: JavaScript BFS solution

var averageOfLevels = function(root) {
  const averages = [];
  const queue = [root];
  while (queue.length) {
    let sum = 0;
    const size = queue.length;
    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      sum += node.val;
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    averages.push(sum / size);
  }
  return averages;
};

// ===================================================


// [AUTHOR]: jesseokeya
// [DESCRIPTION]: Javascript Solution.


var averageOfLevels = function(root) {
    const arr = [root], results = []
    
    while (arr.length) {
        let average = 0
        const length = arr.length
        
        for (let i = 0; i < length; i++) {
            const node = arr.shift()
            average += node.val
            if (node.left) arr.push(node.left)
            if (node.right) arr.push(node.right)
        }
        
        average /= length
        results.push(average)
        
        average = 0
    }
    
    return results
};

// ===================================================


// [AUTHOR]: ybmlk
// [DESCRIPTION]: JavaScript Simple BFS

var averageOfLevels = function(root) {
    
    let queue = [root];
    const average = []
    
    while(queue.length) {
        const next = []
        let sum = 0;
        
        for(let node of queue) {
            sum += node.val;
            if(node.left) next.push(node.left);
            if(node.right) next.push(node.right);
        }
        
        average.push(sum / queue.length)
        queue = next;
    }
    return average;
};

// ===================================================


// [AUTHOR]: Tracy_Zang
// [DESCRIPTION]: Javascript BFS

var averageOfLevels = function(root) {
    var res = [];
    if(!root) return res;
    var queue = [root];
    
    while(queue.length) {
        var size = queue.length;
        var sum = 0;
        for(let i = 0; i<size; i++) {
            var head = queue.shift();
            sum += head.val;
            if(head.left) queue.push(head.left);
            if(head.right) queue.push(head.right);
        }
        res.push(sum/size);
        
    }
    return res;

    
};

// ===================================================

// [AUTHOR]: ME
// [DESCRIPTION]: NOT WORKING
/*
 *  [TESTS]

	[3,9,20,null,null,15,7]
	[1,1]
	[5,14,null,1]
	[3,1,5,0,2,4,6]

 */

var averageOfLevels = function(root) {
    const queue = [ root ];
    const result = [ root.val ];
    
    while (queue.length > 0) {
        let curr = queue.shift();
        
        if (curr.left && curr.right) {
            result.push((curr.left.val + curr.right.val) / 2);
            queue.push(curr.left);
            queue.push(curr.right);
            continue;
        }
        
        if (curr.left) {
            result.push(curr.left.val);
            queue.push(curr.left);
            continue;

        }
        
        if (curr.right) {
            result.push(curr.right.val);
            queue.push(curr.right);
            continue;
        }
    }
    
    return result;
};

// Seconde (use sgallivan's solution as an example)

var averageOfLevels = function(root) {
    const queue = [ root ],
          averages = [];
    
    while (queue.length) {
        let rowSum = 0,
            qLen = queue.length;

        for (let i = 0; i < qLen; i++) {
            let curr = queue.shift();
            rowSum += curr.val;

            if (curr.left) queue.push(curr.left);
            if (curr.right) queue.push(curr.right);
        }

        averages.push(rowSum / qLen);
        
    }
    
    return averages;
};