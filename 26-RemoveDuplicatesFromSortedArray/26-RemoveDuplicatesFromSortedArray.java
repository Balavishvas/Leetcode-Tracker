// Last updated: 7/14/2026, 2:17:08 PM
class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length==0){
            return 0;

        }
        int i=0;
        for(int j=1;j<nums.length;j++){
            if(nums[i]!=nums[j]){
                i=i+1;
                nums[i]=nums[j];
    
            }
        }
        return i+1;
    }
}