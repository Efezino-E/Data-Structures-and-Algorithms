# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # if "depth == 1" create a node with value val as the new root of the original tree
        # such that the original tree is the new root's left subtree
        if depth == 1:
            node = TreeNode(val = val)
            node.left = root
            root = node

        # Get a list of all "curs" (not null nodes at "depth - 1").
        from collections import deque
        stack = deque()
        stack.append((root, 1))
        curs = []

        while len(stack) != 0:
            node, cur_depth = stack.popleft()
            
            if cur_depth >= depth:
                break
            elif cur_depth == depth - 1:
                curs.append(node)
            else:
                l = node.left
                r = node.right
                if l != None:
                    stack.append((l, cur_depth + 1))
                if r != None:
                    stack.append((r, cur_depth + 1))
        
        # Create two nodes for each of the curs with value val
        # cur's original left subtree should be the left subtree of the new left subtree root.
        # cur's original right subtree should be the right subtree of the new right subtree root.

        for cur in curs:
            left_node = TreeNode(val = val)
            right_node = TreeNode(val = val)

            original_left = cur.left
            original_right = cur.right

            left_node.left = original_left
            right_node.right = original_right

            cur.left = left_node
            cur.right = right_node
        
        return root