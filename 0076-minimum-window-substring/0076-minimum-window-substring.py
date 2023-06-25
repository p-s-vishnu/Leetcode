from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        1. I: str, str O: str (min window)
        2. Can have duplicates
        3. TC
            s = "ADOBECODEBANC", t = "ABC"
            s = "ADOBECODEBANCB", t = "ABCB"
        4. Sliding window  O(m), S:O(m)
        """ 
        res, res_len = [-1, -1], float('inf')
        count_t, window = Counter(t), defaultdict(int)
        have, need = 0, len(count_t)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            
            if c in count_t and window[c] == count_t[c]:
                have += 1
        
            while have == need:         # Shrink the window
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1          # pop from the left window
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ''