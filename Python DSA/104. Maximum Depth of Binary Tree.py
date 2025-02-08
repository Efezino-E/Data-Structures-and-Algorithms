# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0

        stack = [(root, 1)] # instantiate the stack with a tuple of node and depth
        max_depth = 1       # set the max depth to 1    

        while len(stack) != 0:                          # while the stack is not empty
            node, depth = stack.pop()                   # get the node and current depth
            l = node.left                               # get the children of the node
            r = node.right

            if l != None:                               # if the children exist, add them to the stack
                stack.append((l, depth + 1))            # along with their depths
                max_depth = max(depth + 1, max_depth)   # update the max depth 
            
            if r != None:
                stack.append((r, depth + 1))
                max_depth = max(depth + 1, max_depth)
                
        return max_depth                                # return the max depth