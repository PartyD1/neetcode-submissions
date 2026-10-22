class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = set()

        #right index - left index + 1 = length of substring

        for right in range(len(s)):
            #right carries index, not value
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            

            seen.add(s[right])

            if longest < right - left + 1:
                longest = right - left + 1

        return longest

