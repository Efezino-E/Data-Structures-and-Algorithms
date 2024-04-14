# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == None and q == None:     # if both nodes are empty return true
            return True                 # if both nodes are not empty continue
        elif p == None or q == None:    # if only one node is empty return false
            return False

        stackp = [p]
        stackq = [q]

        while len(stackp) != 0:         # iterate through the p and q tree and return false where they differe
            if len(stackq) == 0:
                return False
            
            nodep = stackp.pop()
            nodeq = stackq.pop()

            if nodep.val != nodeq.val:
                return False
            
            lp = nodep.left
            lq = nodeq.left
            rp = nodep.right
            rq = nodeq.right

            if lp != None:
                if lq != None:
                    stackp.append(lp)
                    stackq.append(lq)
                else:
                    return False
            else:
                if lq != None:
                    return False
            
            if rp != None:
                if rq != None:
                    stackp.append(rp)
                    stackq.append(rq)
                else:
                    return False
            else:
                if rq != None:
                    return False
        
        return True

            