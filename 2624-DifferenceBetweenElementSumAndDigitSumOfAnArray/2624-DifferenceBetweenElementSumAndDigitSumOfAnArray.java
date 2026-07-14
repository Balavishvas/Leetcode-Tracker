// Last updated: 7/14/2026, 2:15:39 PM
class Solution {
    public int differenceOfSum(int[] nums) {
        int x=0,y=0;
        for(int i=0;i<nums.length;i++){
            x+=nums[i];
            while(nums[i]!=0){
                int temp=nums[i]%10;
                y+=temp;
                nums[i]/=10;
            }
        }
        return x-y;
    }
}