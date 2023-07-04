from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        T:O(m*nlog(n) )
        S:O(1)
        d = {}
        
        for s in strs:
            c = ''.join(sorted(s))
            if c in d:
                d[c].append(s)
            else:
                d[c] = [s]
        
        return d.values()
        
        T:O(m*n )
        S:O(1)
        """
        d = defaultdict(list)
        for s in strs:
            c = [0]*26
            for char in s:
                c[ord(char)-ord('a')] += 1
            d[tuple(c)].append(s) 
        return d.values()