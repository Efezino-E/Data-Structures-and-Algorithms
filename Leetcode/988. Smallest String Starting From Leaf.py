# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # dfs to every leaf node and keep track of value
        stack = [(root, chr(root.val + 97))]
        ans = None

        while len(stack) != 0:
            node, val = stack.pop()
            l = node.left
            r = node.right

            if l != None:
                stack.append((l, chr(l.val + 97) + val))
            if r != None:
                stack.append((r, chr(r.val + 97) + val))
            
            # when at leaf node, check if it is value is the minimum
            if l == None and r == None:
                if ans == None:
                    ans = val
                else:
                    ans = min(ans, val)
            
        return ans