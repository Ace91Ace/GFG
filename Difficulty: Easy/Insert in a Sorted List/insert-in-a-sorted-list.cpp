class Solution {
public:
    Node* sortedInsert(Node* head, int key) {
        Node* x = new Node(key);

        // Case 1: Empty list
        if (head == nullptr) {
            return x;
        }

        // Case 2: Insert at beginning
        if (key <= head->data) {
            x->next = head;
            return x;
        }

        // Case 3: Insert in middle or end
        Node* curr = head;
        while (curr->next != nullptr && curr->next->data < key) {
            curr = curr->next;
        }

        x->next = curr->next;
        curr->next = x;

        return head;
    }
};
