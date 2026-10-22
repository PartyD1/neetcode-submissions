class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        
        
        for left in len(range(s)):
            right = left + 1
            current = set()
            current.add(left)