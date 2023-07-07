1. You can do column wise traversal or transpose
​
```
>>> for elem in zip(*test): print(elem)
...
(1, 3, 5)
(2, 4, 6)
```
​
2. Use defaultdict in cases where you mutable datatypes are being shared
​
**Alternate approach:** Use a list of tuples and check whether all the tuples are unique. Each tuple will be a combination of the character and the index -> row, col,
​
`row//3*3+col//3`