class Solution {
    public int romanToDecimal(String s) {
        HashMap<Character, Integer> roman = new HashMap<>();
        roman.put('I', 1);
        roman.put('V', 5);
        roman.put('X', 10);
        roman.put('L', 50);
        roman.put('C', 100);
        roman.put('D', 500);
        roman.put('M', 1000);

        int ans = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            int n1 = roman.get(s.charAt(i));
            int n2 = roman.get(s.charAt(i + 1));

            if (n1 >= n2) {
                ans += n1;
            } else {
                ans -= n1;
            }
        }

        ans += roman.get(s.charAt(s.length() - 1)); 
        return ans;
    }
}
