from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for v in Counter(nums).values():
            if v >= 2: return True
        return False