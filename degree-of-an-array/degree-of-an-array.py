class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        # contains right_index - left_index + 1, number_of_occurrences for each unique element in list
        candidates = [
            (
                nums.count(n),
                (len(nums) - nums[::-1].index(n) - nums.index(n))
            )
            for n in set(nums)
        ]
        
        return min([cand[1] for cand in candidates if cand[0] == max(candidates)[0]])
