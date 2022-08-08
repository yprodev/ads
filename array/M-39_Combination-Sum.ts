// [AUTHOR] aryanttripathi
// [DESCRIPTION] [C++]|Detailed Explanation w/ TREE DIAGRAM| RECURSION + BACKTRACKING| EACH STEP EXPLAINED
// [LINK] https://leetcode.com/problems/combination-sum/discuss/1777334/C%2B%2BorDetailed-Explanation-w-TREE-DIAGRAMor-RECURSION-%2B-BACKTRACKINGor-EACH-STEP-EXPLAINED

// Check out the link if you need detailed explanation

// ==========================================================================


// [AUTHOR] control_the_narrative
// [DESCRIPTION] JavaScript Clean Backtracking Solution
// [LINK] https://leetcode.com/problems/combination-sum/discuss/662307/JavaScript-Clean-Backtracking-Solution

var combinationSum = function(candidates, target) {
    const result = [];
    
    function permute(arr=[], sum=0, idx=0) {
        if(sum > target) return;
        if(sum === target) result.push(arr);
        
        for(let i = idx; i < candidates.length; i++) {
            permute([...arr, candidates[i]], sum+candidates[i], i);
        }
    }
    permute()
    return result;
};

// ==========================================================================

// [AUTHOR] linfongi
// [DESCRIPTION] JavaScript solution with backtracking
// [LINK] https://leetcode.com/problems/combination-sum/discuss/16757/JavaScript-solution-with-backtracking

function combinationSum(candidates, target) {
  var buffer = [];
  var result = [];
  search(0, target);
  return result;

  function search(startIdx, target) {
    if (target === 0) return result.push(buffer.slice());
    if (target < 0) return;
    if (startIdx === candidates.length) return;
    buffer.push(candidates[startIdx]);
    search(startIdx, target - candidates[startIdx]);
    buffer.pop();
    search(startIdx + 1, target);
  }
}

// ==========================================================================


// [AUTHOR] DBabichev
// [DESCRIPTION] [Python] bactracking solution, explained
// [LINK] https://leetcode.com/problems/combination-sum/discuss/875097/Python-bactracking-solution-explained

/*

This is classical backtracking problem, so let us use BackTr(target, curr_sol, k) function, where:

    1. target is target we need to build, if we get some number, we subtract if from target.
    2. curr_sol is current solution built so far.
    3. k is index in our candidates: each new number we take should have number more or equal than k.

So, no in algorighm we do:

    1. If target == 0, it means we found solution, which is kept in curr_sol, so we add it to self.sol list of all found solutions.
    2. If target if negative or k is more than number of candidates, we need to go back.
    3. Finally, for each candidate index in k,..., we run our function recursively with updated parameters.

Complexity: TBD

class Solution:
    def combinationSum(self, candidates, target):
        def BackTr(target, curr_sol, k):  
            if target == 0:
                self.sol.append(curr_sol)

            if target < 0 or k >= len(candidates):
                return

            for i in range(k, len(candidates)):
                BackTr(target - candidates[i], curr_sol + [candidates[i]], i)

        self.sol = []
        BackTr(target, [], 0)   
        return self.sol

*/

// ==========================================================================


/*

    My NOT working solution. It was just an approach to resolve it.

*/
function combinationSum(candidates: number[], target: number): number[][] {
  for (let i = 0; i < candidates.length; i++) {
    
  }
  
  
};

function rec(
  cands: number[],
  idx: number,
  target: number,
  sumCand: number[] = []
) {
  
  if (target == cands[idx]) {
    sumCand.push(cands[idx]);
    
    return sumCand;
  }
  
  let newTarget = target - cands[idx];
  
  if (newTarget < cands[idx]) {
    let newSumCand = rec(cands, idx + 1)
    return sumCand;
  } else {
    rec()
  }
  
}
