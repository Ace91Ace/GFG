class Solution {
    public int findFloor(int[] arr, int x) {
        // code here
        int n = arr.length;
        int l = 0, r = n-1;
        int res = -1;
        while (l <= r){
            int mid = (l+r)/2;
            if (arr[mid] > x){
                r = mid -1;
            }else{
                res = mid;
                l = mid + 1;
            }
        }
        return res;
    }
}
