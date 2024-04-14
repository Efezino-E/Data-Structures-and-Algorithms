# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        val = 0 # instantiate value
        stack = [root] # instantiate stack with root node

        def leaf(node): # function to check if a node is a leaf node
            if node.left == None and node.right == None:
                return True
            else:
                return False

        while len(stack) != 0:      # While the stack is not empty
            node = stack.pop()      # Let current node be the node popped from the stack

            if node.left:           # Get the left and right nodes if they exist
                l = node.left
                if leaf(l):             # If the left node is a leaf node, add it's value
                    val += l.val
                else:
                    stack.append(l)     # if it is not, add it to the stack

            if node.right:
                r = node.right
                if not leaf(r):         # if the right node is not a leaf node, add it to the stack
                    stack.append(r)

        return val                  # return the value
            