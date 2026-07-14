// Last updated: 7/14/2026, 2:17:17 PM
class Solution {
    public boolean isPalindrome(int x) {
    if(x<0){
        return false;
    }
        int start=x;
        int reverse=0;

    while(x>0){
       int digit=x%10;
        reverse=reverse*10+digit;
        x=x/10;
    }

    return reverse == start;

    }
    
}