class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        for i, n in enumerate(nums):
            if not n == 0:
                continue
            elif i == len(nums)-1:
                return True
            for j in range(i-1, -1, -1):
                if j+nums[j] > i:
                    break
            else:
                return False
        
        return True
                