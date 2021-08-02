class Solution:
    import math
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        return 3 ** int (math.log (n, 3) + 0.5) == n
