class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        1. I: List[int] O:List[int]
        2. no need to reduce winnig asteroid, +ve right -ve left, not 0
        3. TCs
            positive one side, negative other side
            mixed: one after the other 
        4. stack based, T:O(n) S:O(n)
        """
        stack = []
        for a in asteroids:
            while stack and (stack[-1]>0 and a<0):
                if stack[-1] + a > 0:
                    break
                elif stack[-1] + a == 0:
                    stack.pop()
                    break
                else:
                    stack.pop()
            else:
                stack.append(a)
        return stack
            
                    
            