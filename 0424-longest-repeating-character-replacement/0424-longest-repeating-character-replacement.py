class Solution:
    """
    Sliding window
    T:O(n)
    S:O(1)
    """
    
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        max_count = 0
        l = 0
        char_map = {}
        for r, char in enumerate(s):
            char_map[char] = char_map.get(char, 0) + 1
            while (r-l+1) - max(char_map.values()) > k:
                char_map[s[l]] -= 1
                l += 1
            max_count = max(max_count, r-l+1)
        return max_count