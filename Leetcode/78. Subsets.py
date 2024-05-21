class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
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
