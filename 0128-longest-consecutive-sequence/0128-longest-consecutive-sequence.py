class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        T:O(n)
        S:O(n)
        """
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