// Last updated: 7/14/2026, 2:17:07 PM
class Solution {
    public int removeElement(int[] nums, int val) {

        int i=0;
        for(int j=0;j<nums.length;j++){
            if(nums[j]!=val){
            int temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
            i++;
               
            }
        }
        return i;
    }
}