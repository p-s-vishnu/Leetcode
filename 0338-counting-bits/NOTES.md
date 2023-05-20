Bitwise solution
​
https://leetcode.com/problems/counting-bits/discuss/1807954/python-O(n)-solution-using-dp
​
```python
def countBits(self, n: int) -> List[int]:
res = [0]
for i in range(1, n+1):
# divided by 2 term is having similar bin representation as term
# it only differs by insignificant bit
res.append(res[i>>1] + i%2)
return res
```
Other ways
1. using int.bit_count
2. bitwise operation
3. DP approach 1 + out[index - offset]