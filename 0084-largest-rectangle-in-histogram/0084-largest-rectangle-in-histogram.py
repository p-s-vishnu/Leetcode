class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        1. I: List[int], O: int max area
        2. each bar 1, cant be sorted, min 0 heights
        3. [2,1,5,6,2,3]
            []
            [10]
        4. Stack: T:O(n) S:O(n)
        """
        max_ar = -1
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, h0 = stack.pop()
                start = idx
                max_ar = max(max_ar, (i-idx)*h0)
            stack.append((start, h))
            
        for idx, h0 in stack:
            max_ar = max(max_ar, (len(heights)-idx)*h0)
        return max_ar
        