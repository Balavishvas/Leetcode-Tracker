// Last updated: 7/14/2026, 2:15:59 PM
class Solution {
    void dfs(int [][]img,int r,int c,int clr,int oc){
        if(r<0||c<0||r>=img.length||c>=img[0].length||img[r][c]!=oc){
            return;
        }
        img[r][c]=clr;
        dfs(img,r-1,c,clr,oc);
        dfs(img,r,c+1,clr,oc);
        dfs(img,r+1,c,clr,oc);
        dfs(img,r,c-1,clr,oc);
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int oldCol=image [sr][sc];
        if(image[sr][sc]!=color){
            dfs(image,sr,sc,color,oldCol);
        }
        return image;
    }
}