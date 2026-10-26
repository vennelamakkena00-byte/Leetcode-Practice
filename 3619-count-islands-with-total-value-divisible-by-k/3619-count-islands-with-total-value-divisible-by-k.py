from collections import deque

class Solution(object):
    def countIslands(self, grid, k):
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    # Start BFS for a new island
                    current_sum = 0
                    queue = deque([(i, j)])
                    current_sum += grid[i][j]
                    grid[i][j] = 0  # Mark as visited
                    
                    while queue:
                        r, c = queue.popleft()
                        
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                current_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                queue.append((nr, nc))
                                
                    # Check if the total value of the island is divisible by k
                    if current_sum % k == 0:
                        count += 1
                        
        return count