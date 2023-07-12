class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1. I: int, O:List[int] combinations
        2. Valid parethesis, backtracking
        3. 
        4. Brute force: Create all combinations of parentheses and then check isValid
           Backtracking T:O(2^N) S:O(N)
            
        """
        res = []
        stack = []
        
        def backtrack(o_count, c_count):
            if o_count == c_count == n:
                res.append(''.join(stack))
            if o_count < n:
                stack.append('(')
                backtrack(o_count+1, c_count)
                stack.pop()
            if c_count < o_count:
                stack.append(')')
                backtrack(o_count, c_count+1)
                stack.pop()
        
        backtrack(0, 0)
        return res