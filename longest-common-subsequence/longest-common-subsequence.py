class Solution:   
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        meme = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for row in range(1, len(text1) + 1):
            for col in range(1, len(text2) + 1):
                if text1[row - 1] == text2[col - 1]:
                    meme[row][col] = 1 + meme[row - 1][col - 1]
                else:
                    meme[row][col] = max(meme[row][col - 1], meme[row - 1][col])
        
        return meme[len(text1)][len(text2)]