class MyStack {
    // class StackNode {
    //     int data;
    //     StackNode next;
    //     StackNode(int a) {
    //         data = a;
    //         next = null;
    //     }
    // }
    StackNode top;

    // Function to push an integer into the stack.
    void push(int a) {
        // Add your code here
        StackNode new_node = new StackNode(a);
        if (top==null){
            top = new_node;
        }
        new_node.next = top;
        top = new_node;
    }

    // Function to remove an item from top of the stack.
    int pop() {
        // Add your code here
        if (top == null){
            return -1;
        }
        int res = top.data;
        top = top.next;
        return res;
    }
}