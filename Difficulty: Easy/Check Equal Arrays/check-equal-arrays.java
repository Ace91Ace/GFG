class Solution {
    public static boolean checkEqual(int[] a, int[] b) {
        // code here
        HashMap<Integer, Integer> c1 = new HashMap<>();
        HashMap<Integer, Integer> c2 = new HashMap<>();
        int la = a.length, lb = b.length;
        
        if (la != lb){
            return false;
        }
        
        for (int i = 0;i < la; i++){
            c1.put(a[i], c1.getOrDefault(a[i], 0)+1);
            c2.put(b[i], c2.getOrDefault(b[i], 0)+1);
        }
        
        return c1.equals(c2);
    }
}