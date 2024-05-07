class Solution:
    def removeNodes(self, head):
        # first reverse the Linked list
        head = self.reverse(head)

        # iterate through the linked list and
        # delete nodes which are less than the 
        # maximum node value we have experienced so far
        cur = head
        while cur != None and cur.next != None:
            if cur.next.val >= cur.val:
                cur = cur.next
            else:
                cur.next = cur.next.next
        
        return self.reverse(head)
    
    def reverse(self, head):
        # linked list must have at least two nodes to be reversed
        if head == None or head.next == None:
            return head

        # make the head node the tail
        node1 = head
        node2 = head.next
        node1.next = None

        # reverse the list by iteratively reversing the connect between every node
        # and storing the node that would been lost by reversing the connection
        while True:
            store = node2.next
            node2.next = node1
            node1 = node2
            node2 = store
            if node2 == None:
                break
        
        # return the new head
        return node1