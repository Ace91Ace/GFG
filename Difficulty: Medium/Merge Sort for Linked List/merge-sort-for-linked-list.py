'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
import heapq

class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        # code here
        hp = []
        curr = head
        while curr:
            hp.append([curr.data, curr])
            curr = curr.next
            
        hp.sort(key = lambda x: x[0])
        dummy = Node(-1)
        curr = dummy
        
        for node in hp:
            curr.next = node[1]
            curr = curr.next
        curr.next = None
        return dummy.next