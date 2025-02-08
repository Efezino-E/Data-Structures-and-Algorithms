class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        # any two nodes are connected
        # you can XOR a path between two nodes and it will end up with those two nodes alone being XOR(ed) as XOR on a value twice cycles
        # therefore the problem becomes we can select any two nodes and XOR them to increase the value, find the maximum value obtainable

        # first we calculate by how much will each node increase
        change = []
        for i in range(len(nums)):
            change.append((nums[i] ^ k) - nums[i])
        
        # sort the changes from maximum to minimum, we want to select node pairs with the largest change
        change.sort(reverse = True)

        # select the nodes in pairs and increase the sum value if possible
        # return the value when there can be no more increases
        value = sum(nums)

        for i in range(0, len(change) - 1, 2):
            delta = change[i] + change[i + 1]
            if delta > 0:
                value += delta
            else:
                return value
        
        return value