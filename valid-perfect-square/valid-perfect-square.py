class Solution:
    def isPerfectSquare_babylonian(self, num: int) -> bool:
        guess = num / 2
        
        while abs(guess*guess - num) > 0.1:
            guess = (guess + num/guess) / 2
        
        if (int(guess)*int(guess) == num):
            return True
    
        return False
    
    def isPerfectSquare_binary(self, num: int) -> bool:
        low = 1
        high = num
        
        while low <= high:
            mid = int(0.5*(low + high))
            if mid*mid < num:
                low = mid + 1
            elif mid*mid > num:
                high = mid - 1
            else:
                return True
            
        return False
    
    def isPerfectSquare(self, num: int) -> bool:
        return self.isPerfectSquare_binary(num)