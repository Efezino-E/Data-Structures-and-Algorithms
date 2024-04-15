# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        stack = [root]

        val = 0
        while len(stack) != 0:
            node = stack.pop()
            l = node.left
            r = node.right

            if l != None:
                l.val = node.val * 10 + l.val
                if l.left == None and l.right == None:
                    val += l.val
                else:
                    stack.append(l)

            if r != None:
                r.val = node.val * 10 + r.val
                if r.left == None and r.right == None:
                    val += r.val
                else:
                    stack.append(r)
        
        return val
