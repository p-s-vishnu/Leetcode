from collections import defaultdict

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        """
        1. I: (List[int] x 4), O: int (min cost)
        2. min cost, rowCosts & colCosts, cost can be 0
        3. ([1,0], [2,3], [5,4,3], [8,2,6,7])
            bot already at home
            reverse of house and bot
        4. BFS with caching T:O(m*n) S:O(m*n)
            Optimal: Geometry -> walk in shortest path and calculate cost
            
        5. Time limit exceed for the below
            R, C = len(rowCosts), len(colCosts)
            min_cost = sum(rowCosts) + sum(colCosts)
            visited = set()
            def bfs(r,c):
                q = deque([(r,c, 0)])
                while q:
                    r0, c0, cost = q.popleft()

                    if [r0, c0] == homePos:
                        nonlocal min_cost
                        min_cost = min(cost, min_cost)
                        continue
                    if (r0, c0) in visited: continue  
                    visited.add((r0, c0))
                    if r0 > 0:      q.append((r0-1, c0, cost+rowCosts[r0-1]))
                    if r0 < R-1:    q.append((r0+1, c0, cost+rowCosts[r0+1]))
                    if c0 > 0:      q.append((r0, c0-1, cost+colCosts[c0-1]))
                    if c0 < C-1:    q.append((r0, c0+1, cost+colCosts[c0+1]))

            bfs(startPos[0], startPos[1])
            return min_cost
        """
        min_cost = 0
        rowdir = 1 if startPos[0] < homePos[0] else -1
        coldir = 1 if startPos[1] < homePos[1] else -1
        for r in range(startPos[0], homePos[0], rowdir):
            min_cost += rowCosts[r+rowdir]
            
        for c in range(startPos[1], homePos[1], coldir):
            min_cost += colCosts[c+coldir]
        return min_cost
        
        