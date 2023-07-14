class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        T:O(n)
        S:O(1)
        
        def isalnum(char):
            return (ord('A') <= ord(char) <= ord('Z')) or (ord('a') <= ord(char) <= ord('z')) or (ord('0') <= ord(char) <= ord('9'))
        """
        if len(s) < 2:  return True
        l, r = 0, len(s)-1
        while l < r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r > -1 and not s[r].isalnum():
                r -= 1
            if l < len(s) and r > -1 and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
        