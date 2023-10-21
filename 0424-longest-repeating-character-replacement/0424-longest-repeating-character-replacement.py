from collections import defaultdict
class Solution:
    """
    Sliding window
    T:O(n)
    S:O(26) => O(1)
    """
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2: return len(s)

        l = maxf = max_count = 0
        counter = defaultdict(int)
        for r, char in enumerate(s):
            counter[char] += 1
            maxf = max(counter[char], maxf)
            while (r-l+1) - maxf > k:
                counter[s[l]] -= 1
                l += 1
            max_count = max((r-l+1), max_count)
        return max_count