class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        1. I:List[int] O:int (num_fleets)
        2. faster but previous car will not cross the forward one
            , position[i] < target, position are unique
            single car is also a fleet
        3. target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
            None catch up
            All get stuck and move
        4. Sort positions and use stack or last time T:O(nlogn) S:O(n or 1)
            Key: iterate right to left
        """
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        count = 0
        curr = 0
        for t in reversed(times):
            if t > curr:
                count += 1
                curr = t
        return count