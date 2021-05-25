class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:    
        magic_triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1*nums[i]
            start, end = i+1, len(nums)-1
            while start < end:
                if nums[start] + nums[end] == target:
                    magic_triplets.append([nums[i],nums[start],nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1        
        
        return magic_triplets

    