// Last updated: 7/14/2026, 2:17:22 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
     boolean []arr=new boolean[256];
     int right=0;
     int left=0;
     int Lenmax=0;

     while(right<s.length()){
        char c=s.charAt(right);
        while(arr[c]){
            arr[s.charAt(left)]=false;
        left++;
            
        }
        arr[c]=true;
        Lenmax=Math.max(Lenmax,right-left+1);
        right++;
    }
    return Lenmax;
    }
}