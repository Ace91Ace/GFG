class Solution {
    public Node reverse(Node start, Node end, Node p, Node temp) {
        if (start == null) return null;
        Node prev = p;
        Node curr = start;

        while (curr != temp) {
            Node nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
        }
        return prev;
    }

    public Node reverseKGroup(Node head, int k) {
        if (head == null || k <= 1) return head;

        Node dummy = new Node(-1);
        dummy.next = head;
        Node prev = dummy;
        Node curr = head;

        while (curr != null) {
            Node start = curr;
            Node end = curr;

            for (int i = 1; i < k && end.next != null; i++) {
                end = end.next;
            }

            Node temp = end.next;
            Node newH = reverse(start, end, prev, temp);

            prev.next = newH;
            prev = start;
            start.next = temp;
            curr = start.next;
        }
        return dummy.next;
    }
}
