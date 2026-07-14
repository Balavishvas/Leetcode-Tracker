// Last updated: 7/14/2026, 2:17:24 PM
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] arr = new int[2];
        for (int i = 0; i < nums.length;i++){
            for (int j = 1; j < nums.length;j++) {
                if(i!=j){
                if ((nums[i] + nums[j]) == target) {
                    arr[0] = i;
                    arr[1] = j;
                }
                }
            }
        }
        return arr;
    }
}