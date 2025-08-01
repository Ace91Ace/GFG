class Solution {
    public double medianOf2(int a[], int b[]) {
        int al = a.length, bl = b.length;
        int totalLen = al + bl;
        int mid = totalLen / 2;

        if (al == 0) {
            if (bl % 2 != 0) return b[mid];
            return (b[mid] + b[mid - 1]) / 2.0;
        }
        if (bl == 0) {
            if (al % 2 != 0) return a[mid];
            return (a[mid] + a[mid - 1]) / 2.0;
        }

        int[] ans = merged(a, b);
        if (totalLen % 2 != 0) {
            return ans[mid];
        } else {
            return (ans[mid] + ans[mid - 1]) / 2.0;
        }
    }
    
    private int[] merged(int[] left, int[] right) {
        int l = 0, r = 0, k = 0;
        int[] merge = new int[left.length + right.length];
        
        while (l < left.length && r < right.length) {
            if (left[l] <= right[r]) {
                merge[k++] = left[l++];
            } else {
                merge[k++] = right[r++];
            }
        }
        while (l < left.length) {
            merge[k++] = left[l++];
        }
        while (r < right.length) {
            merge[k++] = right[r++];
        }
        
        return merge;
    }
}
