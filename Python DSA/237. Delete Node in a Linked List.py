# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # assign current node to given node
        cur = node

        while True:
            # assign the values of the next node to current node
            if cur.next:
                cur.val = cur.next.val

            # if the next node is the last node, unlink the node and break the iteration
            if cur.next.next == None:
                cur.next = None
                break

            # effect the iteration by changing the current node to the next node for the next loop
            cur = cur.next