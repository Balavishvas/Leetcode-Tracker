// Last updated: 7/14/2026, 2:17:00 PM
class Solution {
public int jump(int[] nums) {
        int  jumps=0 ,end=0 ,count=0;
        for(int i=0;i<nums.length-1;i++){
            count=Math.max(count,i+nums[i]);
            if(i==end){
                jumps++;
                end =count;
            }
        }
        return jumps;
    }

}
        

