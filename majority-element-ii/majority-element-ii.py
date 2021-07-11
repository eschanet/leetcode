class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return list(set(nums))
        
        ans = set()
        cnt = 1
        prev = sorted(nums)[0]
        for n in sorted(nums)[1:]:
            if n == prev:
                cnt += 1
            else: 
                cnt = 1
            if cnt > len(nums)//3:
                ans.add(n)
            prev = n

        return list(ans)
                        