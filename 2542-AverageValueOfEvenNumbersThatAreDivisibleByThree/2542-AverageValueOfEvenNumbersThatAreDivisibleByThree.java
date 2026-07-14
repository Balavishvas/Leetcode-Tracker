// Last updated: 7/14/2026, 2:15:38 PM
class Solution {
    public int averageValue(int[] nums) {
        int n=0;int a=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2==0 && nums[i]%3==0){
                n+=nums[i];
                a++;
            }
        }
        if(n==0) return 0;
        return n/a;
    }
}