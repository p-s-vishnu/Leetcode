class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
            
        #left product
        for i in range(1, len(output)):
            output[i] = output[i-1]*nums[i-1]
        # right product
        prev = 1    # product so far
        for i in range(-1, -len(output)-1, -1):
            output[i] = prev*output[i]
            prev *= nums[i]
        return output