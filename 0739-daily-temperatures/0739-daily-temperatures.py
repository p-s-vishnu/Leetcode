class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        1. I: List[int] -> Temp difference, O: List[int] -> Days
        2. answer[i] == 0 if no future
        3.  mixed with +ves and 0
            0 with 
        4. Brute force T:O(n2) S:O(1)
            Extra memory T:O(n) S:O(n)
        """
        out = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, idx = stack.pop()
                out[idx] = i - idx
            stack.append((t, i))
        return out