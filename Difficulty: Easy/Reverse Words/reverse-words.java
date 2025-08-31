import java.util.*;

class Solution {
    public String reverseWords(String s) {
        String[] res = s.split("\\.+");
        List<String> x = new ArrayList<>();
        
        for (String w : res) {
            if (!w.isEmpty()) {   
                x.add(w);
            }
        }
        
        Collections.reverse(x);
        return String.join(".", x);
    }
}
