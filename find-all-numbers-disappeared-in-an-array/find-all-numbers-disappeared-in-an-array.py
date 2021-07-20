class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique_nums = set(nums)
        ans = set()
        for n in range(1,len(nums)+1):
            if not n in unique_nums:
                ans.add(n)
        
        return list(ans)
