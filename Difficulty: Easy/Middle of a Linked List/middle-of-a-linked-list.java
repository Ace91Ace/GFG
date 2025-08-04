/* Node of a linked list
 class Node {
   int data;
    Node next;
    Node(int d)  { data = d;  next = null; }
}
*/

class Solution {
    int getMiddle(Node head) {
        // Your code here.
        Node sl = head, fs = head;
        while (fs != null && fs.next != null){
            sl = sl.next;
            fs = fs.next.next;
        }
        return sl.data;
    }
}