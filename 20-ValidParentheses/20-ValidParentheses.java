// Last updated: 7/14/2026, 2:17:18 PM
class Solution {
    public boolean isValid(String s) {
        char arr[]=new char[s.length()];
        int ind=-1;
        for(char ch:s.toCharArray()){
            if (ch=='('){
                arr[++ind]=')';
            }
            else if(ch=='{'){
                arr[++ind]='}';
            }
            else if(ch=='['){
                arr[++ind]=']';

            }
            else if(ind==-1){
                return false;
            }
            else if(arr[ind--]!=ch){
                return false;
            }
        }
        return ind==-1;
       }
}