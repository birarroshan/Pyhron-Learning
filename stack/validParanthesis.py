class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            match i:
                case ")":
                    if not stack or stack[-1] != "(":
                        return False
                    stack.pop()
                case "}":
                    if not stack or stack[-1] != "{":
                        return False
                    stack.pop()
                case "]":
                    if not stack or stack[-1] != "[":
                        return False
                    stack.pop()
                case _:
                    stack.append(i) 
        return not stack


s = Solution()
print(s.isValid('()[]{}'))
print(s.isValid('['))
print(s.isValid(']'))