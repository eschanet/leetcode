class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        return [
            self.find_start_index(nums,target),
            self.find_end_index(nums,target)
        ]
    
    
    def find_start_index(self, nums: List[int], target: int) -> int:
        start, stop = 0, len(nums)-1
        index = -1
        
        while start <= stop:
            
            mid = (start + stop) // 2

            if nums[mid] == target:
                index = mid
                stop = mid-1
            elif target < nums[mid]:
                stop = mid-1
            else:
                start = mid+1
        
        return index
    
    
    def find_end_index(self, nums: List[int], target: int) -> int:
        start, stop = 0, len(nums)-1
        index = -1
        
        while start <= stop:
            
            mid = (start + stop) // 2

            if nums[mid] == target:
                index = mid
                start = mid+1
            elif target < nums[mid]:
                stop = mid-1
            else:
                start = mid+1
        
        return index