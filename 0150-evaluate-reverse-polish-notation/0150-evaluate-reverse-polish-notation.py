class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        1. I: List[str] O: int computed value
        2. Reverse poish notation, always valid expression
           Digits: [-200, 200]
        3. two digits then operator
            all digits first then all operator
        4. Brute force T:O(n) S:O(n)
        """
        def isoperator(o):
            return o in {'+', '-', '*', '/'}
        
        stack = []
        for t in tokens:
            if not isoperator(t):
                stack.append(t)
            else:
                a = stack.pop() 
                b = stack.pop() 
                out = int(eval(b+t+a))
                stack.append(str( out ))
        return int(stack[0])
            