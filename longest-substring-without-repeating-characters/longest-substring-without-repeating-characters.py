class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        start, max_length = 0, 0
        
        for i, c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            seen[c] = i
            
        return max_length