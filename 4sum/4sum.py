class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        magic_quadruplets = []
        nums.sort()
        
        # break down to 3SUM
        for i in range(len(nums)):            
            # break down to 2SUM
            for j in range(i, len(nums)):
                if j == i: 
                    continue

                new_target = target-nums[i]-nums[j]
                start, end = j+1, len(nums)-1

                while start < end:
                    if nums[start] + nums[end] == new_target:
                        magic_quadruplets.append([nums[i],nums[j],nums[start],nums[end]])
                        start += 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                    elif nums[start] + nums[end] < new_target:
                        start += 1
                    else:
                        end -= 1        

                                
        # remove unnecessary entries
        seen = []
        result = []
        for quadruplet in magic_quadruplets:
            if not sorted(quadruplet) in seen:
                result.append(quadruplet)
                seen.append(sorted(quadruplet))

        return result

    