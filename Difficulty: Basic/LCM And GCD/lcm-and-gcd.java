class Solution {
    public static int gcdd(int a, int b){
            if (b==0){
                return a;
            }
            return gcdd(b, a%b);
        }
    public static int[] lcmAndGcd(int a, int b) {
        // code here
        int gcd = gcdd(a, b);
        int lcm = (int)((a*b)/gcd);
        
        int[] res = {lcm, gcd};
        return res;
        
    }
}