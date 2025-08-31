/*Complete the function(s) below*/
class GfG {
    public void push(int a, Stack<Integer> s) {
        // add code here.
        s.push(a);
    }

    public int pop(Stack<Integer> s) {
        // add code here.
        if (s.isEmpty()) return -1;
        int res = s.pop();
        return res;
    }

    public int min(Stack<Integer> s) {
        // add code here.
        Stack<Integer> temp = new Stack<>();
        int mn = 100000;
        while (!s.isEmpty()){
            int e = s.pop();
            mn = Math.min(mn, e);
            temp.push(e);
        }
        while (!temp.isEmpty()){
            s.push(temp.pop());
        }
        return mn;
    }

    public boolean isFull(Stack<Integer> s, int n) {
        // add code here.
        return (n == s.size());
    }

    public boolean isEmpty(Stack<Integer> s) {
        // add code here.
        return s.isEmpty();
    }
}