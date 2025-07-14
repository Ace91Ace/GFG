def quickSort(head):
    #return head after sorting
    hp = []
    curr = head
    while curr:
        hp.append([curr.data, curr])
        curr = curr.next
    
    hp.sort(key = lambda x: x[0])
    dummy = Node(-1)
    curr = dummy
    
    for i in hp:
        curr.next = i[1]
        curr = curr.next
    curr.next = None
    return dummy.next
    