class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # determine the number of rows and columns
        num_rows = len(grid)
        num_cols = len(grid[0])

        # initalize score by forcing the element of the first column to be all 1's
        score = num_rows * (2 ** (num_cols - 1))

        # iterate through every column but the first
        for col in range(1, num_cols):
            # find out the binary exponent number (the last column is 0)
            exp = num_cols - 1 - col

            # initialize a count of true ones and true zeros
            true_ones = 0
            true_zeros = 0

            # determine the number of true ones and zeros for this column
            for row in range(num_rows):
                if grid[row][col] == grid[row][0]:
                    true_ones += 1
                else:
                    true_zeros += 1
            
            # update score based on majority
            score += max(true_ones, true_zeros) * (2 ** exp)
        
        # return score
        return score
        