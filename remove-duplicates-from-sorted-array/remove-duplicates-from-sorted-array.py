class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        orig_len = len(nums)
        
        for i in range(len(nums)-1, 0, -1):
            print(i)
            if nums[i] == nums[i-1]:
                del nums[i]
        
        k = len(nums)
        nums.extend(['_'] * (orig_len - k))
        
        return k
