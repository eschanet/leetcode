class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum(map(lambda x: x**2, [int(d) for d in str(n)]))
            if n in seen and n != 1:
                return False
            seen.add(n)
        
        return True