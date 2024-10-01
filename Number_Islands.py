def numIslands(grid) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def dfs(r, c):
        # Check for out of bounds and water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        # Mark the land as visited
        grid[r][c] = '0'
        # Explore all four directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found an island
                num_islands += 1
                dfs(r, c)  # Visit all connected land

    return num_islands

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
# Each cell is visited once.

# Space Complexity: O(m * n) for the recursion stack in the worst case (if all cells are land).
# In the iterative BFS approach, space complexity would be O(min(m, n)) for the queue.
