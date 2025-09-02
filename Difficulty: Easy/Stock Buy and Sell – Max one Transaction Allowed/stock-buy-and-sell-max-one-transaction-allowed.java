// User function Template for Java
import java.util.*;
class Solution {
    public int maximumProfit(int prices[]) {
        // Code here
        int n = prices.length;
        ArrayList<Integer> suffix = new ArrayList<>(Collections.nCopies(n, 0));
        
        int mx = prices[n-1];
        suffix.set(n-1, mx);
        for (int i = n-2; i >= 0; i--){
            mx = Math.max(prices[i], mx);
            suffix.set(i, mx);
        }
        int res = 0;
        for (int i = 0; i < n; i++){
            res = Math.max(res, suffix.get(i)-prices[i]);
        }
        return res;
    }
}