# Last updated: 7/23/2026, 12:38:45 PM
1class Solution:
2  def compress(self, chars: List[str]) -> int:
3    ans = 0
4    i = 0
5
6    while i < len(chars):
7      letter = chars[i]
8      count = 0
9      while i < len(chars) and chars[i] == letter:
10        count += 1
11        i += 1
12      chars[ans] = letter
13      ans += 1
14      if count > 1:
15        for c in str(count):
16          chars[ans] = c
17          ans += 1
18
19    return ans