class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if not stack:
                    return False
                current_pop = stack.pop()
                if i == ")" and current_pop != "(":
                    return False
                if i == "}" and current_pop != "{":
                    return False
                if i == "]" and current_pop != "[":
                    return False
                    
        
        if not stack:
            return True