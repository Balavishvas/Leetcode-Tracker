# Last updated: 7/14/2026, 2:17:15 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total=0

        for i in range(len(s)):
            current=roman[s[i]]

            if i < len(s)-1 and current < roman[s[i+1]]:
                total -=current
            else:
                total +=current
            
        return total
        