class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        links = {} # dictionary to store linked files
        m = len(grid)
        n = len(grid[0])

        def link(i, j): # function to link all the land appropriately from grid
            if grid[i][j] == "0":
                return
            
            links[(i, j)] = []
            neighbors = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
            valid_neighbors = []

            for neighbor in neighbors:
                if neighbor[0] >= 0 and neighbor[0] <= m - 1:
                    if neighbor[1] >= 0 and neighbor[1] <= n - 1:
                        if grid[neighbor[0]][neighbor[1]] == "1":
                            valid_neighbors.append(neighbor)

            for neighbor in valid_neighbors:
                links[(i, j)].append((neighbor[0], neighbor[1]))
            
            return

        for i in range(m): # linking all lands
            for j in range(n):
                link(i, j)
                
        available_land = list(links.keys())

        def delete_patch(touched): # function to delete every land connected to a touched land
            linked_lands = [touched]
            while len(linked_lands) != 0:
                parent = linked_lands.pop()
                if (parent[0], parent[1]) in links:
                    children = links[(parent[0], parent[1])]
                    for child in children:
                        linked_lands.append(child)
                links.pop((parent[0], parent[1]), None)

        island = 0
        while len(available_land) != 0: # while lands are available
            touched = available_land.pop() # touch a land
            delete_patch(touched) # delete lands connected to touched lands from available lands
            island += 1 # update island explored
            available_land = list(links.keys()) # update available lands

        
        return island # reutnr islands explored

    # this can be implemented shorter without storing links and directly deleting connecting lands
