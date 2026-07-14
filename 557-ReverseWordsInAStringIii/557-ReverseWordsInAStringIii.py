# Last updated: 7/14/2026, 2:16:05 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        ans=[]

        for word in s:
            ans.append(word[::-1])
            result=" ".join(ans)
        return result