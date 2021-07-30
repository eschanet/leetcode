class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps,idx = [],0
        
        while idx < len(nums)-1:
            curr_max = 0
            jumps.append(nums[idx])

            for i in range(idx,idx+nums[idx]+1):
                if i >= len(nums)-1:
                    return len(jumps)
                elif i+nums[i] > curr_max:
                    curr_max = i+nums[i]
                    idx = i


        return len(jumps)
        