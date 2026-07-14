// Last updated: 7/14/2026, 2:16:29 PM
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for(int i=1;i<nums.length;i++){
            if(nums[i]==nums[i-1]){
            return true;
             }
}
    return false;
    }
}