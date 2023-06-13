class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        T:O(n)
        S:O(n)
        if not nums:
            return 0
        numsset = set(nums)
        global_max = 0

        for n in numsset:
            if (n-1) not in numsset:
                counter = 0
                while (n+counter) in numsset:
                    counter += 1
                global_max = max(global_max, counter)	
        return global_max
        """
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best