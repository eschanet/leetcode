class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mighty_dict = {nums[i] : i for i in range(len(nums))}

        for i in range(len(nums)):
            r = target - nums[i]
            match = mighty_dict.get(r) 
            if match and match != i:
                return [i, match]