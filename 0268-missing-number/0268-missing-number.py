class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
    
        # Index sort
        for i in range(n):
            while nums[i] < n and i != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(n):
            if nums[i] != i:
                return i
        return n