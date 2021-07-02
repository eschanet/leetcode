class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
#         # contains right_index - left_index + 1, number_of_occurrences for each unique element in list
#         candidates = [
#             (
#                 nums.count(n),
#                 (len(nums) - nums[::-1].index(n) - nums.index(n))
#             )
#             for n in set(nums)
#         ]
        
#         return min([cand[1] for cand in candidates if cand[0] == max(candidates)[0]])
        
        
        # not as nice, but hopefully faster
        occurrences = {}
        indices = {}
        for idx, n in enumerate(nums):
            if n in occurrences:
                indices[n].append(idx)
                occurrences[n] += 1
            else:
                indices[n] = [idx]
                occurrences[n] = 1
        
        return min([
            idx[-1] - idx[0] + 1 
            for n, idx in indices.items() 
            if occurrences[n] == max(occurrences.values())
        ])            