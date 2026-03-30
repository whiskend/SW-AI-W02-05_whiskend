if canvisited[i]:
            for j in range(1, jump_num+1):        
                dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1