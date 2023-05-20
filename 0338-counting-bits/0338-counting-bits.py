class Solution:
    def countBits(self, n: int) -> List[int]:
        # out = [0]*(n+1)
        # for i in range(1, n+1):
        #     out[i] = 1 + out[i-offset]
        # return out
        out = [0]*(n+1)
        for i in range(1, n+1):
            out[i] = 1 + out[i- 2**int(log(i,2))]
        return out
        
        