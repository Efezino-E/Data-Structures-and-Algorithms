class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        # initiate result as a grid of zeros
        n = len(grid)
        import numpy as np
        result = np.zeros((n, n), dtype = int)

        # compute the maxLocal for each cell in the result grid and return
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                result[i][j] = self.maxLocal(grid, i, j)
        
        # remove the extra rows and columns
        return result[1 : n - 1, 1 : n - 1]
    
    def maxLocal(self, grid, m, n):
        # initiate the max local as the most negative number and the kernel size
        ans = - float("inf")
        kernel_size = 1

        # calculate the max local using the kernel size for the cell and return
        for i in range(m - kernel_size, m + kernel_size + 1):
            for j in range(n - kernel_size, n + kernel_size + 1):
                ans = max(ans, grid[i][j])

        return ans