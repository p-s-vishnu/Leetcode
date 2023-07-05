T: O(n) S:O(n)
​
- A variant of bucket sort
​
**Core idea:** Use list indexes as a proxy to keep top k values and length of array is bucket array list
​
https://leetcode.com/problems/top-k-frequent-elements/solutions/2506883/python-o-n-o-n/?q=O%28N%29&orderBy=most_relevant
​
**Common heap operations**
​
1. heappop(list)
2. heappush(list, val)
3. heapreplace() is equivalent to heappop() followed by heappush().
4. heappushpop() is equivalent to heappush() followed by heappop().
5. merge(), the input is a generator
6. nlargest()
​
```
if k == len(nums):
return nums
# build hash map: char and how often it appears
count = Counter(nums)