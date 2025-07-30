'''

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        def revers(node):
            prev = None
            curr = node
            while curr:  
                nxt = curr.next  
                curr.next = prev  
                prev = curr
                curr = nxt  
            return prev

        if not head or not head.next:  
            return True

        sp, fp = head, head

        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next

        curr = revers(sp)
        curr1 = head

        while curr and curr1:
            if curr1.data != curr.data:
                return False
            curr = curr.next
            curr1 = curr1.next

        return True

        
        