from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        1. I:List[List[int]] [[start,end]] O: bool
        2. at most one edge, no cycle
        3. normal
            cycle
            no connection
            source and destination equal
        4. DFS or BFS
            T: O(v + e)
            S: O(v + e)
        """
        def dfs(s) ->bool:
            stack = [s]
            visited = set()
            while stack:
                n = stack.pop()
                if n == destination:
                    return True
                if n not in visited:
                    visited.add(n)
                    stack.extend(list(d[n]))
            return False
        
        d = defaultdict(set)
        for s,e in edges:
            d[s].add(e)
            d[e].add(s)     
        return dfs(source)