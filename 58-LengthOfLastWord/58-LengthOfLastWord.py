# Last updated: 7/14/2026, 2:16:55 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        count=len(s[-1])
        return count
            