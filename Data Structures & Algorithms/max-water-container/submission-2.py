class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float('-inf')

        left, right = 0,len(heights)-1

        while left < right:
            min_index = min(heights[left], heights[right])
            distance = right - left
            area = distance * min_index
            if max_area < area:
                max_area = area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return max_area