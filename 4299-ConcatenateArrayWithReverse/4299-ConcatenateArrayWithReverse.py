# Last updated: 7/14/2026, 2:15:41 PM
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return (nums+nums[::-1])
        
        