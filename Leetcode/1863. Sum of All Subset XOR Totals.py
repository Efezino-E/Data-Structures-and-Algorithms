class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def dfs(i, total):
            if i == len(nums):
                return total
            
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)
        
        return dfs(0,0)