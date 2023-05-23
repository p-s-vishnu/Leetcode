You need to know the below functions
- zfill(32)
- int("1010101", 2)  # binary to decimal
- format(int , 'b') or bin(int)
​
"""python
1. normal approach
2. Use zfill(), zero fill
3. Bitwise operation
int(bin(n)[2:].zfill(32)[::-1], 2)
"""
return int(format(n, 'b').zfill(32)[::-1], 2)
​
Optimised solution for 32 bit
```
n&0xffff0000>>16 | n&0x0000ffff<<16
n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
```
[LC](https://leetcode.com/problems/reverse-bits/discuss/54741/O(1)-bit-operation-C%2B%2B-solution-(8ms))
[Video link](https://www.youtube.com/watch?v=-5z9dimxxmI)
​
Solutions