class Solution {
    public boolean isPalinSent(String s) {
        // code here
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int l = 0, r = s.length()-1;
        while (l < r){
            if (s.charAt(l) != s.charAt(r)){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}