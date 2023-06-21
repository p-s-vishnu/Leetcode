class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window problem
        """
        if len(s) < 2:
            return len(s)
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
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = -1
        longest = 0
        alphabets = {}
        for r in range(len(s)):
            if (s[r] in alphabets) and alphabets[s[r]] > l:
                l = alphabets[s[r]]
            alphabets[s[r]] = r
            longest = max(longest, r-l)
        return longest
"""
