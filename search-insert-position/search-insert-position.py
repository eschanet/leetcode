class Solution:    
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        
        start, stop = 0, len(nums)
        i = (stop - start) // 2
        
        while not (nums[i] < target and nums[i+1] > target) :
            print(i)
            if target > nums[i]:
                start, stop = i, stop
            else:
                start, stop = start, i
            i = (stop - start) // 2 + start

        return i+1