# Last updated: 7/14/2026, 2:15:57 PM
class Solution:
    def fib(self, n: int) -> int:
        
            if n<=1:
                return n
            else: 
                return self.fib(n-1) + self.fib(n-2)
    
        