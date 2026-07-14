# Last updated: 7/14/2026, 2:16:36 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        l=0
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l=l+1
            r=r-1
        l=0
        r=k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l=l+1
            r=r-1
        l=k
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l=l+1
            r=r-1