class Solution:
    def minPathLength(self, grid: list[list[int]], start, end):
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        
        return grid[end[0]][end[1]]

# Example usage
grid = [
    [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]
]
solution = Solution()
start = (0, 0)
end = (3, 3)
print(solution.minPathLength(grid, start, end)) 
