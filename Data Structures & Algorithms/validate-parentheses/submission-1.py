class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1 or len(s) % 2 != 0:
            return False

        closed_dict = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in closed_dict:
                if not stack or stack[-1] != closed_dict[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack
