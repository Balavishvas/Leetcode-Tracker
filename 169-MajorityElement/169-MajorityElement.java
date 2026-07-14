// Last updated: 7/14/2026, 2:16:37 PM
class Solution {
    public int majorityElement(int[] nums) {
        int candi=0;
        int points=0;

        for(int i=0;i<nums.length;i++){
            if(points==0){
                candi=nums[i];
            }
            if(candi==nums[i]){
                points++;

            }
            else{
                points--;
            }
        }
        return candi;
    }
}