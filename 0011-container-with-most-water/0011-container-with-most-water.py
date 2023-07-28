class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        1. I: List[int] height, O: int (max area)
        2. container cannot be slant, min 2 lines
        3. [1,8,6,2,5,4,8,3,7]
            Only two [9,1]
            equal [1,8,6,2,5,4,8,3,8]
        4. Two pointer T:O(n) S:O(1)
        """
        maxArr = -1
        l, r = 0, len(height)-1
        while l < r:
            maxArr = max(maxArr, (r-l)*min(height[l], height[r]))
            if height[l] > height[r]: r -= 1
            else: l += 1
        return maxArr
            