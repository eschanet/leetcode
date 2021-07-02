# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        if guess(n) == 0 : return n
        
        start, stop = 1, n
        mid = (start + stop) // 2
        
        g = guess(mid)
        
        while g != 0:
            print(start, mid, stop)

            if g == 1:
                start, stop = mid+1, stop
            elif g == -1:
                start, stop = start, mid
            else:
                break
        
            mid = (start + stop) // 2
            g = guess(mid)
            
            
        return mid