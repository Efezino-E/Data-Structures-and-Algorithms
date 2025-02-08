# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: [ListNode]) -> [ListNode]:
        # reverse the list node and multiply it by 2 according to normal math
        head = self.reverse(head)
        carry = 0
        cur = head

        while cur != None:
            node_val = cur.val
            val = 2 * node_val + carry
            cur.val = val % 10
            carry = val // 10
            last = cur
            cur = cur.next
        
        if carry != 0:
            last.next = ListNode(carry)
            
        return self.reverse(head)

    def reverse(self, head):
        # there must be at least two nodes to reverse the order of a linked list
        if head == None or head.next == None:
            return head
        
        node1 = head
        node2 = head.next
        node1.next = None

        while True:
            store = node2.next
            node2.next = node1
            node1 = node2
            node2 = store
            if node2 == None:
                break
        
        return node1