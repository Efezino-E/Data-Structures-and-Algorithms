# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # recursively join the leaft nodes
        if root.val == 0:
            return False
        
        elif root.val == 1:
            return True
        
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        
        
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)