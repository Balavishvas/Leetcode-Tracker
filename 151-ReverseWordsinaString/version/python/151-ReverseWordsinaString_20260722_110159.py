# Last updated: 7/22/2026, 11:01:59 AM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        S=s.split()
4        for word in S:
5            res= " ".join(S[::-1])
6        return (res)