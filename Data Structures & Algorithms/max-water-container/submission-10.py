class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area, left, right = 0, 0, len(heights) - 1
        while left < right:
            max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return max_area