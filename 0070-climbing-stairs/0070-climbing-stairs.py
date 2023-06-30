class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1. I:n O: num of ways 
        2. Constraints
        3. TC
        4. Patterns: Divide nd conquer
            Top down
            
            Current: Bottom up
        5. Psuedo code: T:O(n) S:O(n)
        
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        """
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        first, second = 1, 2
        for i in range(3, n+1):
            second, first = first + second, second
        return second