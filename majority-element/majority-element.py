class Solution:
    
    import collections
    
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[0][0]
