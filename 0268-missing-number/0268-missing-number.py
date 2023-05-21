class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing

#         n = len(nums)
    
#         # Index sort
#         for i in range(n):
#             while nums[i] < n and i != nums[i]:
#                 nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

#         for i in range(n):
#             if nums[i] != i:
#                 return i
#         return n