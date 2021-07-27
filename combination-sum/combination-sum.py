class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        
        def combinations(i: int, path: List[int]):
            
            if sum(path) == target:
                ans.append(path[:])
                return
            elif sum(path) > target:
                return
            
            for n in range(i,len(candidates)):
                path.append(candidates[n])
                combinations(n,path)
                path.pop()
            
        combinations(0,[])
        return ans