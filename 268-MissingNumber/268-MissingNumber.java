// Last updated: 7/14/2026, 2:16:16 PM
class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
        int expectednum=n*(n+1)/2;
        int actualnum=0;

        for(int num:nums){
                actualnum+=num;
        }

    return expectednum-actualnum;
    }
}