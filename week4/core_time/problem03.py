def numIslands(grid):
    if not grid: return 0
    
    m, n = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        # 범위를 벗어나거나 물('0')인 경우 종료
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0':
            return
        
        # 방문한 땅은 '0'으로 바꿔서 재방문 방지
        grid[r][c] = '0'
        
        # 상하좌우 탐색
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c) # 연결된 모든 땅 지우기
                
    return count