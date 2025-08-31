/*
class Node
{
    int data;
    Node next;

    Node(int key)
    {
        data = key;
        next = null;
    }
}
*/
import java.util.*;
class Solution {
    public static int fractional_node(Node head, int k) {
        // Your code here
        int l = 0;
        Node curr = head;
        while (curr != null){
            l += 1;
            curr = curr.next;
        }
        curr = head;
        double x = Math.ceil((double)l/k);
        for (int i=1; i < x; i++){
            curr = curr.next;
        }
        return curr.data;
    }
}