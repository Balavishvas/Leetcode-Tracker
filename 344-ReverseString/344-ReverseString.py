# Last updated: 7/14/2026, 2:16:13 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
"""
        stack=[]

        for i in s:
            stack.append(i)
        
        i=0
        while len(stack)>0:
            a=stack.pop()
            s[i]=a
            i+=1
        return stack