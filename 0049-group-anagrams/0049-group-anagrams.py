from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            c = ''.join(sorted(s))
            if c in d:
                d[c].append(s)
            else:
                d[c] = [s]
        
        return d.values()