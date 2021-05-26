import itertools

class Solution:
    
    def my_permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            yield nums
        else:
            for permutation in self.my_permute(nums[1:]):
                for i in range(len(nums)):
                    yield permutation[:i] + nums[0:1] + permutation[i:]
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # the lazy/smart way
        # return [list(p) for p in list(itertools.permutations(nums))]
        
        # the hard way
        answer = []
        for perm in self.my_permute(nums):
            answer.append(perm)
        return answer
    