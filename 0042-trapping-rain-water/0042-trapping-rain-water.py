class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1. I: List[int] (height), O:int(total water)
        2. elevation map, width=1, min=1 map
        3. Normal [5,4,3,3,0,1]
            Useless edges [0,1,0,2,1,0,1,3,2,1,2,1]
            0 water & single value [0,0,0,0,0]
        4. Idea: know water retention at each point
            Prefix and suffix array T:O(n) S:O(n)
            Two pointer T:O(n) S:O(1)
            
        5. Prefix/Stack
            def get_cumulative_max(arr):
                out = []
                max_so_far = 0
                for h in arr:
                    out.append(max_so_far)
                    max_so_far = max(max_so_far, h)
                return out

            totAr = 0
            maxL = get_cumulative_max(height)
            maxR = get_cumulative_max(height[::-1])[::-1]
            for i, h in enumerate(height):
                totAr += max(min(maxL[i], maxR[i])-h, 0)
            return totAr
        """
        if len(height) <= 2: return 0
        l, r = 0, len(height)-1
        totAr = 0
        maxL, maxR = height[l], height[r]
        
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                totAr += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                totAr += maxR - height[r]
        return totAr
        