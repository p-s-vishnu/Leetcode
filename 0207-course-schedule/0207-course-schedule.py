class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map course to prerequisites
        prereq = {n:[] for n in range(numCourses)}
        for c,p in prerequisites:
            prereq[c].append(p)
        
        # visited set and perform dfs 
        visited = set()
        def dfs(c):
            if c in visited:    # if visited in the DFS search
                return False
            if prereq[c] == []:
                return True
            
            visited.add(c)
            for pre in prereq[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)
            prereq[c] = []
            return True
            
        # visit all nodes and DFS
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True