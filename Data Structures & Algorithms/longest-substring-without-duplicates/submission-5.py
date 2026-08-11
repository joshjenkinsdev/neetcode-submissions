class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left, ans = 0, 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1 
            window.add(s[right])
            ans = max(ans, len(window))
        
        return ans