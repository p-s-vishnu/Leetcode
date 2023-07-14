class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        T:O(n)
        S:O(1)
        """
        def isalnum(char):
            # 0:48, A:65, a:97
            # 9:57, Z:90, z:122
            return (ord('A') <= ord(char) <= ord('Z')) or \
                    (ord('a') <= ord(char) <= ord('z')) or \
                    (ord('0') <= ord(char) <= ord('9'))
        
        if len(s) < 2:  return True
        l, r = 0, len(s)-1
        while l < r:
            while l < len(s) and not isalnum(s[l]):
                l += 1
            while r > -1 and not isalnum(s[r]):
                r -= 1
            if l < len(s) and r > -1 and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
        