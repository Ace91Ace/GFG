// User function Template for Java

class Solution {
    // Function to check if we can reach the last index from the 0th index.
    public boolean canReach(int[] arr) {
        // code here
        int ml = -1, n = arr.length;
        if (n == 1) return true;
        if (arr[0] == 0) return false;
        
        for (int i=0; i < n-1; i++){
            if (arr[i] == 0 && ml <= i){
                return false;
            }
            ml = Math.max(ml, arr[i]+i);
            if (ml >= n-1){
                return true;
            }
        }
        return false;
    }
}