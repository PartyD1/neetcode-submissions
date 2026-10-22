class Solution:
    def isValid(self, s: str) -> bool:
        paren = []
        curly = []
        square = []

        for i in s: 
            if i == "(":
                paren.append("(")
            elif i == ")":
                if not paren:
                    return False
                paren.pop()
            elif i == "{":
                curly.append("{")
            
            elif i == "}":
                if not curly:
                    return False
                curly.pop()

            elif i == "[":
                square.append("[")

            elif i == "]":
                if not square:
                    return False
                square.pop()
        
        if not paren and not curly and not square:
            return True

        return False

    