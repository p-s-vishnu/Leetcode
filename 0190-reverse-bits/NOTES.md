You need to know the below functions
- zfill(32)
- int("1010101", 2)  # binary to decimal
- format(int , 'b') or bin(int)
​
​
1. Use zfill(), zero fill
3. Bitwise operation
​
​
Approach1: Brute force
```
#int(bin(n)[2:].zfill(32)[::-1], 2)
return int(format(n, 'b').zfill(32)[::-1], 2)
```
​
Approach2: bitwise approach
```python
res = 0
for i in range(32):
bit = (n >> i) & 1
res = res | (bit<<(31-i))
# res |= ((n >> i) & 1) << (31-i)
return res
```
​
Optimised solution for 32 bit
```
n&0xffff0000>>16 | n&0x0000ffff<<16