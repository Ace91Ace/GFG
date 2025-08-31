class Solution {
    static boolean isPrime(int n) {
        // code here
        int r = (int)(Math.sqrt(n));
        if (n == 1) return false;
        for (int i=2; i <= r+1; i++){
            if (n%i == 0){
                return false;
            }
        }
        return true;
    }
}