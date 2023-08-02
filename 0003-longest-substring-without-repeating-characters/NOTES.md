> Lookup method will not work eg: "dvdf" it will be cleared at steo 3 but it will exclude the elem just before
​
**T:O(n), S:O(n or 1) Approach 1** as the dict will have a maximum of 26 letters counter
​
- Have a left / start pointer which will act as an anchor to calculate the length
- Issue:
- the anchor needs to be updated if it encounters a duplicate character, new position should be one index more.
- **DO NOT UPDATE** if the `index in dict < start`. If the prev occurence of current character is at bigger index than left/start/anchor index it means that we will have to disregard all that before the anchor index. If the prev occurence is before the left then we do not need to update as it will not be used in the length calculation.
- Global max to keep track of maximum/longest substring
​
**Reference**: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1737/C%2B%2B-code-in-9-lines.
​
**Approach 2: Two-pointer / Sliding Window
T:O(n), S:O(n or 1) **
​
- Create an array / dict to store the count of alphabets seen till now
- Increment as you see the character
- but if the character is > 1 then while it is false do the following