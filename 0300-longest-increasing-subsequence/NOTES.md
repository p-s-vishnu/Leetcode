Memoization

T:O(nlogn), S:O(1) 


https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326552/Optimization-From-Brute-Force-to-Dynamic-Programming-Explained


General DP explanation: https://www.youtube.com/watch?v=aPQY__2H3tE


nlogn: https://www.youtube.com/watch?v=0wT67DOzqBg


nlogn with space 1: https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326552/Optimization-From-Brute-Force-to-Dynamic-Programming-Explained!
```python
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = 0
        for cur in nums:
            if length == 0 or nums[length-1] < cur:
                nums[length] = cur
                length += 1
            else:
                idx = bisect_left(nums, cur, 0, length)
                nums[idx] = cur
        return length

```
