class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        1. I: List[int] O:List[int]
        2. no need to reduce winnig asteroid, +ve right -ve left, not 0
        3. 
            positive one side, negative other side
            mixed: one after the other 
        4. stack based, T:O(n) S:O(n)
            two pointer?
        """
        def collide(a, stack):
            while stack and (stack[-1]>0 and a<0):
                if stack[-1] + a > 0:
                    return
                elif stack[-1] + a == 0:
                    stack.pop()
                    return
                else:
                    stack.pop()
            else:
                stack.append(a)
        
        stack = []
        for a in asteroids:
            if stack and (stack[-1]>0 and a<0):
                collide(a, stack)
            else:
                stack.append(a)
        return stack
            
                    
            