import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two pointer, T:O(n), S:O(1)
        Bisect?
        """
        l = 0
        r = bisect.bisect(numbers, target-numbers[l])
        if r >= len(numbers): r -= 1
        
        while l < r:
            if numbers[l]+numbers[r] == target:
                break
            elif numbers[l]+numbers[r] < target:
                l += 1
            else:
                r -= 1
        return [l+1,r+1]
        