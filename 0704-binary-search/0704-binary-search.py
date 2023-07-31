class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1: return -1
        l,r = 0, len(nums)-1
        while l < r:
            mid = (r+l)//2
            if target > nums[mid]: l = mid + 1
            else: r = mid
        return l if nums[l] == target else -1
        