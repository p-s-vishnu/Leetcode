from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        T: (klogn)
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        
        return heapq.nlargest(k, count.keys(), key = count.get)
        
        T:O(n)
        S:O(n)
        """
        if k == len(nums):
            return nums
        freq = [[] for _ in range(len(nums)+1)]
        c = Counter(nums)
        for key,v in c.items():
            freq[v].append(key)
            
        result = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                result.append(n)
                
                if len(result) == k:
                    return result