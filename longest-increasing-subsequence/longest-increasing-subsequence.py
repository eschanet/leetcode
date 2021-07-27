class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        length = [1] * len(nums)

        for i in range(1,len(nums)):    
            subproblems = [length[k] for k in range(i) if nums[k] < nums[i]]
            length[i] = 1 + max(subproblems, default=0)
        return max(length, default=0)