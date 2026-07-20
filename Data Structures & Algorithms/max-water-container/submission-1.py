class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = float('-inf')

        left, right = 0,len(heights)-1

        while left < right:
            min_index = min(heights[left], heights[right])
            distance = right-left
            if area < distance * min_index:
                area = distance * min_index

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return area