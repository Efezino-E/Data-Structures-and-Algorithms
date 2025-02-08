class Solution(object):
    def subsets(self, nums):
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # === ITERATIVE SOLUTION ===
        """
        # Initialize empty subset
        subset = [[]]

        # for each number we consider, we add it to all existing subsets
        # and also keep the original subsets existing before adding that number
        # we continue this till we exhaust all numbers

        for num in nums:
            to_add = []

            for array in subset:
                to_add.append(array + [num])

            subset += to_add
            
        return subset

        # === BACKTRACKING SOLUTION ===
        """
        # initialize subset
        subset = []
        subsets = []

        # create a dfs to add the current element to the each array in the subset as new arrays
        def dfs(i):
            if i == len(nums):
                subsets.append(subset[:])
                return 
            
            else:
                subset.append(nums[i])
                dfs(i + 1)

                subset.pop()
                dfs(i + 1)
        
        dfs(0)

        return subsets"""
