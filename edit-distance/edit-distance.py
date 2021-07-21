class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        
        # initialise the DP map
        dp_map = [[0 for i in range(l2+1)] for j in range(l1+1)]
        for i in range(1,l1+1):
            dp_map[i][0] = i
        for j in range(1,l2+1):
            dp_map[0][j] = j
        
        # bottom-up approach
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                dp_map[i][j] = min(
                    dp_map[i-1][j] + 1,
                    dp_map[i][j-1] + 1,
                    dp_map[i-1][j-1] + 1 if word1[i-1] != word2[j-1] else dp_map[i-1][j-1]
                )
        
        # import pprint
        # pprint.pprint(dp_map)
        
        return dp_map[l1][l2]
        