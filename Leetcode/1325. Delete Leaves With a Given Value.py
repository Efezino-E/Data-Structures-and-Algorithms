# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        # if the node is empty, return it as empty back
        if root == None:
            return None
            
        # update the left and right sub tree
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # after updating, if the left and right subtree are empty
        # and the current node is the target, delete the node
        if root.left == None and root.right == None:
            if root.val == target:
                return None

        return root