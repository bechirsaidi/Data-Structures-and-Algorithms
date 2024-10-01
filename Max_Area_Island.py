def maxAreaOfIsland(grid):
    # Define dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    # Function to perform DFS to find the area of an island
    def dfs(r, c):
        # Check if the current position is out of bounds or water (0)
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0
        
        # Mark the current cell as visited by setting it to 0
        grid[r][c] = 0
        
        # Calculate the area by exploring all four directions
        area = 1
        area += dfs(r + 1, c)  # Down
        area += dfs(r - 1, c)  # Up
        area += dfs(r, c + 1)  # Right
        area += dfs(r, c - 1)  # Left
        
        return area

    max_area = 0
    
    # Iterate over all cells in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Perform DFS to calculate the area of this island
                max_area = max(max_area, dfs(r, c))
    
    return max_area
def test_maxAreaOfIsland():
    # Test case 1: Example case with multiple islands
    grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    assert maxAreaOfIsland(grid1) == 6, "Test case 1 failed"
    
    # Test case 2: Grid with no land
    grid2 = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]
    assert maxAreaOfIsland(grid2) == 0, "Test case 2 failed"
    
    # Test case 3: Single cell island
    grid3 = [[1]]
    assert maxAreaOfIsland(grid3) == 1, "Test case 3 failed"
    
    # Test case 4: Large single island
    grid4 = [[1,1,1],
             [1,1,1],
             [1,1,1]]
    assert maxAreaOfIsland(grid4) == 9, "Test case 4 failed"
    
    # Test case 5: Mixed grid with multiple small islands
    grid5 = [[1,0,1,0,1],
             [0,1,0,1,0],
             [1,0,1,0,1]]
    assert maxAreaOfIsland(grid5) == 1, "Test case 5 failed"
    
    print("All test cases passed!")

# Run the tests
test_maxAreaOfIsland()
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
# This is because in the worst case, we visit every cell once.

# Space Complexity: O(m * n) for the recursion stack in the worst case if the entire grid is one large island.
