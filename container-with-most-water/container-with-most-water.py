class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def compute_area(left: int, right: int) -> int:
            return (right - left) * min(height[left], height[right])
        
        left, right = 0, len(height) - 1
        area = 0
        
        while left < right:
            area = max(area,compute_area(left,right))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
