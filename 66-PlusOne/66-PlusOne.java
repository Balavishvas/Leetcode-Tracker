// Last updated: 7/14/2026, 2:16:52 PM
class Solution {
    public int[] plusOne(int[] digits) {
        for(int i=digits.length-1;i>=0;i--){
            if(digits[i]+1<10){
                digits[i]++;
                return digits;
            }else{
             digits[i]=0;
            }
        }
    int newarr[]=new int[digits.length+1];
    newarr[0]=1;
    return newarr;
    }}