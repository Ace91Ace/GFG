/*
class Node {
    int data;
    Node next;
    Node prev;

    Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}
*/
class Solution {
    public Node reverse(Node head) {
        // code here
        Node prv = null;
        Node curr = head;
        
        while (curr != null){
            Node temp = curr.next;
            curr.next = prv;
            curr.prev = temp;
            prv = curr;
            curr = temp;
        }
        return prv;
    }
}