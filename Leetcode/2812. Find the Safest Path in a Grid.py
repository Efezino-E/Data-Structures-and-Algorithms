class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        def getChildren((row, col)): # O(1)
            """
            Returns a list of tuples which are valid children of a cell (i, j)
            """
            # initialize array to store children
            children = []

            # iterate through all child nodes and append them if they are within bounds
            for i, j in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if min(i, j) >= 0 and max(i, j) < N:
                    children.append((i, j))
            
            return children
        
        def updateGrid(grid): # O(N^2)
            """
            Updates the grid values to contain the minimum distance to the closest cell with the value 1
            """
            # find all ones in the grid
            ones = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        ones.append((i, j))
                        grid[i][j] = 0
            
            # perform multiple breadth first searches starting the ones as root nodes
            # and update the grid distances
            from collections import deque
            store = set(ones)
            children = deque(ones)
            visited = {}

            while len(children) > 0:
                cur = children.popleft()
                curs_children = getChildren(cur)
                val = grid[cur[0]][cur[1]]

                for child in curs_children:
                    if child not in visited and child not in store:
                        visited[child] = True
                        grid[child[0]][child[1]] = val + 1
                        children.append(child)
            
            return grid

        # if the last or first cell is a thief return 0
        if grid[N - 1][N - 1] == 1 or grid[0][0] == 1:
            return 0

        # update the grid and initialize the search constraints
        # we'll implement a Djkistra algorithm that prioritizes the max values
        # as we only care about the path the maximum of the minimum safe value 
        # rather than the total aggregated safe value
        grid = updateGrid(grid)
        children = [(-grid[0][0], 0, 0)]
        visited = {(0, 0): True}
        num = 0

        while len(children) > 0:
            cur = heapq.heappop(children)
            val = -cur[0]
            i = cur[1]
            j = cur[2]

            if val == 0:
                return 0
            
            elif i == N - 1 and j == N - 1:
                return val
            
            else:
                curs_children = getChildren((i, j))
                for child in curs_children:
                    if child not in visited:
                        visited[child] = True
                        heapq.heappush(children, (-min(val, grid[child[0]][child[1]]), child[0], child[1]))
                num += 1