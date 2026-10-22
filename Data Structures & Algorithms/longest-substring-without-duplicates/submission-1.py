class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left = 0
        #s = "xxyxx"
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            
            if longest < (right - left + 1):
                longest = (right - left + 1)
            
        return longest