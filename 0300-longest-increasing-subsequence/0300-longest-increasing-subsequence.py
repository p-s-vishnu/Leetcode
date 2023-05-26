class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        T:O(n2)
        S:O(n)
        """
        L = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    L[i] = max(L[i], 1+L[j])
        return max(L, default=0)