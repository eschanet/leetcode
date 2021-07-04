class Solution:
    def fib(self, n: int) -> int:
            
        meme = {}

        def get_fib(n: int) -> int:
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
        
        return get_fib(n)