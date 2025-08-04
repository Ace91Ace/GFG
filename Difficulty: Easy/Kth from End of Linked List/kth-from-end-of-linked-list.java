/* Structure of node
class Node
{
    int data;
    Node next;
    Node(int d) {data = d; next = null; }
} */

class Solution {

    // Function to find the data of kth node from
    // the end of a linked list.
    int getKthFromLast(Node head, int k) {
        // Your code here
        int l = 0;
        Node curr = head;
        while (curr != null){
            l++;
            curr = curr.next;
        }
        if (k > l){
            return -1;
        }
        int x = l - k;
        curr = head;
        for (int i = 0; i < x; i ++){
            curr = curr.next;
        }
        return curr.data;
    }
}