# Last updated: 7/14/2026, 2:16:19 PM
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        total=self.sumDigits(num)
        return self.addDigits(total)
    def sumDigits(self,n):
        if n==0:
            return 0
        return n%10 + self.sumDigits(n//10)

        