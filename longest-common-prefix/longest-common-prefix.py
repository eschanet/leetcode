class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        if not len(shortest) > 0: return ""
        if all([s.startswith(shortest) for s in strs]): return shortest

        i = len(shortest) // 2
        left, right = shortest[0:i], shortest[i:len(shortest)]
        previous = ''
        
        while previous != left:
            # print(previous, left,right)
            previous = left
            if all([s.startswith(left) for s in strs]):    
                left += right[0 : len(right)//2]
                right = right[len(right)//2 : len(right)]
            else:
                right = left[3*len(left)//4 : len(left)]
                left = left[0 : 3*len(left)//4]
            
        return left