1. Bottom-up approach: https://www.youtube.com/watch?v=Y0lT9Fck7qI
​
Fibonacci approach https://www.youtube.com/watch?v=RrFg9SZ8VoM
​
S:O(1) approach
​
```python
a, b = 1, 1+n%2
for i in range(n//2):
a += b
b += a
return a
```