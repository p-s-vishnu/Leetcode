class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        1. I: string, O:int (count)
        2. substring, duplicate palindromes acceptable
        3.  aa O:3
            aba O:4
        4. 2 pointer T:O(n2), S:O(1)
        """
        counter = 0 # visited = set()

        def compute(l,r):
            nonlocal counter
            while l>=0 and r<len(s) and s[l] == s[r]:
                counter += 1    # visited.add((l,r))
                l -= 1
                r += 1

        for i in range(len(s)):
            compute(i, i)       # for odd lens
            compute(i, i+1)     # for even len
            
        return counter # len(visited)