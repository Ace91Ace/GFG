class Solution {
    public static int[] lcmAndGcd(int a, int b) {
        // code here
        int x = Math.max(a, b), y = Math.min(a, b);
        while(y != 0){
            int temp = y;
            y =  x%y;
            x = temp;
        }
        int gcd = x;
        int lcm = (int)((a*b)/gcd);
        
        int[] res = {lcm, gcd};
        return res;
        
    }
}