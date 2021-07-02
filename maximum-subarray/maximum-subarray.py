class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subsum = nums[0]
        curr_subsum = nums[0]
        
        for n in nums[1:]:
            curr_subsum = max(n, curr_subsum + n)
            max_subsum = max(max_subsum, curr_subsum)
            
        return max_subsum