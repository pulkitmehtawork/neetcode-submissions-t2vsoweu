class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c,visited ):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 
            if grid[r][c] == "0":
                return 
            if (r, c ) in visited:
                return 
            visited.add((r,c))
            dfs(r+1 , c, visited)
            dfs(r-1 , c,visited)
            dfs(r , c+1,visited)
            dfs(r , c-1,visited)





        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c,visited)
                    cnt +=1
        return cnt