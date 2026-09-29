class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for k in (-1, 1):
                if -1 < i + k < m:
                    dfs(i + k, j)
                if -1 < j + k < n:
                    dfs(i, j + k)
                    
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands