class Solution:
    def tribonacci(self, n: int) -> int:
        meme = {}
                
        def trib_bottomup(n: int) -> int:
            meme[0], meme[1], meme[2] = 0, 1, 1
            for i in range(3, n+1):
                meme[i] = meme[i-1] + meme[i-2] + meme[i-3] 
            return meme[n]
        
        return trib_bottomup(n)