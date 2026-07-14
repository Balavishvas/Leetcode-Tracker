# Last updated: 7/14/2026, 2:16:45 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        for i in s:
            if i.isalnum():
                temp.append(i.lower())
        
        return temp==temp[::-1]