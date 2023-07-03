class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Use a dictionary single pass - T:O(n) S:O(n)
        """
        d = {}
        for idx, n in enumerate(nums):
            if n in d:
                return [d[n], idx]
            d[target - n] = idx