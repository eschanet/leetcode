class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]
        
        # no need to pad the list, just return k
        return len(nums)