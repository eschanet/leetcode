import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in list(itertools.permutations(nums))]
        
        