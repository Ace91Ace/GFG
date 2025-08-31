/* Structure of LinkedList
class Node
{
    int data;
    Node next;
    Node(int d)
    {
        data = d;
        next = null;
    }
}
*/
class Solution {
    boolean isCircular(Node head) {
        // Your code here
        Node tgt = head;
        Node curr = head;
        
        while(curr != null){
            curr = curr.next;
            if (curr == tgt){
                return true;
            }
        }
        return false;
    }
}