import java.util.HashMap;
import java.util.Map;

class Solution {
    public static boolean areAnagrams(String s1, String s2) {
        // code here
        Map<Character, Integer> c = new HashMap<>();
        Map<Character, Integer> b = new HashMap<>();
        for (char i : s1.toCharArray()){
            c.put(i, c.getOrDefault(i, 0)+ 1);
        }
        for (char i : s2.toCharArray()){
            b.put(i, b.getOrDefault(i, 0)+ 1);
        }
        return c.equals(b);
    }
}