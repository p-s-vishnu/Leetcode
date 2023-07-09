class Solution:
    def isValid(self, s: str) -> bool:
        """
        T:O(n)
        S:O(n)
        """
        if len(s) == 0: return True
        if len(s) < 2: return False
        br_map = {
            "]":"[",
            "}": "{",
            ")": "("
        }
        stack = []
        for bracket in s:
            if bracket in {'(', '[', '{'}:
                stack.append(bracket)
            elif len(stack) < 1 or (br_map.get(bracket) != stack.pop()):
                return False
        return not stack