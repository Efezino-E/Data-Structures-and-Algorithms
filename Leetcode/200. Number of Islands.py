class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        links = {}
        m = len(grid)
        n = len(grid[0])

        def land(i, j):
            return grid[i][j] == 1

        def link(i, j):
            links[(i, j)] = []

            if not land(i, j) == 0:
                return
            
            neighbors = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
            valid_neighbors = []

            for neighbor in neighbors:
                if neighbor[0] >= 0 and neighbor[0] <= m - 1:
                    if neighbor[1] >= 0 and neighbor[1] <= n - 1:
                        valid_neighbors.append(neighbor)
            
            for neighbor in valid_neighbors:
                links[(i, j)].append((neighbor[0], neighbor[1]))
            
            return

        for i in range(m):
            for j in range(n):
                link(i, j)
                
        available_land = list(links.keys())

        def delete_patch(touched):

            linked_lands = [touched]
            while len(linked_lands) != 0:
                parent = linked_lands.pop()
                links.pop((parent[0], parent[1]))
                children = links[(parent[0], parent[1])]
                for child in children:
                    linked_lands.append(child)

        island = 0
        while len(available_land) != 0:
            touched = available_land.pop()
            delete_patch(touched)
            island += 1
        
        return island