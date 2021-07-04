class Solution:
    def fib(self, n: int) -> int:
            
        meme = {}

        def fib_recur(n: int) -> int:
            if n in meme:
                return meme[n]
            if n == 0:
                res = 0
            elif n == 1 or n == 2:
                res = 1
            else:
                res = get_fib(n-1) + get_fib(n-2)
            meme[n] = res
            return res
        
        def fib_bottomup(n: int) -> int:
            meme[0] = 0
            meme[1] = 1
            
            for i in range(2, n+1):
                meme[i] = meme[i-1] + meme[i-2]
            
            return meme[n]
        
        return fib_bottomup(n)