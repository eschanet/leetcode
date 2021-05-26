class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if not nums[i] in (nums[:i]+nums[i+1:]):
                return nums[i]