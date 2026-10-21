class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for c in s:
            if c.isalnum():
                cleaned_s += c.lower()
                
        s = cleaned_s


        for i in range(len(s)):
            if s[i] != s[~i]:
                return False
            continue 
        
        return True