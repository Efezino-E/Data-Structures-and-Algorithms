class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # initialize the number of rows and cols
        nrows = len(grid)
        ncols = len(grid[0])

        # initialize the max gold collected
        maxGoldCollected = 0

        # perform a dfs with every node as a root and return the one with max gold collected
        for row in range(nrows):
            for col in range(ncols):
                maxGoldCollected = max(maxGoldCollected, self.getMaxPathThroughPoint(grid, (row, col)))
        return maxGoldCollected
    
    def getValidChildren(self, grid, (row, col)):
        """
        Returns the valid children of a cell in a grid
        """
        # add children to the array if their index is within bounds and their value is not zero
        children = []

        for i in (row - 1, row + 1):
            if not (i < 0 or i >= len(grid)):
                if grid[i][col] != 0:
                    children.append((i, col))
        
        for j in (col - 1, col + 1):
            if not (j < 0 or j >= len(grid[0])):
                if grid[row][j] != 0:
                    children.append((row, j))
        
        return children

    def getMaxPathThroughPoint(self, grid, (row, col)):
        """
        Returns the maximum path with a point as the head using dfs
        """
        # get the valid children of the current node
        children = self.getValidChildren(grid, (row, col))

        # store the current node value
        store = grid[row][col]

        # mark the node as visited
        grid[row][col] = 0

        # initiate the maxGold stored
        maxGold = store

        # perform the dfs recursively
        for childRow, childCol in children:
            maxGold = max(maxGold, store + self.getMaxPathThroughPoint(grid, (childRow, childCol)))
        
        # return the grid back to it's original state so that another node can be used for the call
        grid[row][col] = store

        # return the maxGold collected
        return maxGold