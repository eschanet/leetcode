class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        
        if numRows == 1:
            return ans[:1]
        elif numRows == 2:
            return ans
        
        for i in range(2,numRows):
            curr_row = list(map(sum, zip(ans[i-1], ans[i-1][1:])))      
            ans.append([1]+curr_row+[1])
        
        return ans
            