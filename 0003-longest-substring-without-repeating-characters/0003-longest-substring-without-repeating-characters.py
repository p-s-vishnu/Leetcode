class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        T: O(n) S:(n or 26->1)
        
        """
        if len(s) < 2: return len(s)
        l = longestSubstr = -1
        num_idx_map = {}
        for r in range(len(s)):
            if s[r] in num_idx_map and num_idx_map[s[r]] > l:   l = num_idx_map[s[r]]
            num_idx_map[s[r]] = r
            longestSubstr = max(longestSubstr, r-l)
        return longestSubstr
        
        
        """
        Alternate Sliding window problem using sets
        if len(s) < 2: return len(s)
        l = 0
        longest = 0
        visited = set()
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            longest = max(longest, r-l+1)
        return longest
        """
