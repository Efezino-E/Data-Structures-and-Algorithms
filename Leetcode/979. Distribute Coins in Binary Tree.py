# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # starting from the bottom nodes
        # we know the amount of flow needed to make them all 1 gold
        # we take this flow to the next layer
        # and iteratively do this up till to the root node
        # we sum up the total flows needed

        # initiate total flows as zero
        self.res = 0

        def distributeExtraCoins(cur):
            
            # if the current node is a Null node, flow needed is 0
            if cur == None:
                return 0
            
            # the flow needed for a node is the flow from it's left, right and itself
            left_extra = distributeExtraCoins(cur.left)
            right_extra = distributeExtraCoins(cur.right)
            curs_extra = cur.val - 1 + left_extra + right_extra

            # we don't care if the flow is away or into the node for our final result
            self.res += abs(curs_extra)

            # we care about direction for our iteration
            return curs_extra
        
        # perform the distribution
        distributeExtraCoins(root)

        # return the ans
        return self.res