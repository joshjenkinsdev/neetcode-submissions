class Solution:
    def maxArea(self, heights: List[int]) -> int:
        slow, fast = 0, 1
        max_area = 0
        while slow < fast and slow < len(heights) - 1:
            area = min(heights[slow], heights[fast]) * (fast - slow)
            if area > max_area:
                max_area = area
            if fast == len(heights) - 1:
                slow += 1
                fast = slow + 1
            else:
                fast+=1
        return max_area