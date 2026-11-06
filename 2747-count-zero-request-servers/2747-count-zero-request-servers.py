class Solution(object):
    def countServers(self, n, logs, x, queries):
        # Sort logs by time
        logs.sort(key=lambda item: item[1])
        
        # Pair each query with its original index so we can restore the order later
        indexed_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        res = [0] * len(queries)
        server_count = {}
        active_servers = 0
        
        left = 0
        right = 0
        m = len(logs)
        
        for q_idx, q_time in indexed_queries:
            start_time = q_time - x
            end_time = q_time
            
            # Expand the window to the right (include logs with time <= end_time)
            while right < m and logs[right][1] <= end_time:
                server_id = logs[right][0]
                if server_count.get(server_id, 0) == 0:
                    active_servers += 1
                server_count[server_id] = server_count.get(server_id, 0) + 1
                right += 1
                
            # Shrink the window from the left (remove logs with time < start_time)
            while left < m and logs[left][1] < start_time:
                server_id = logs[left][0]
                server_count[server_id] -= 1
                if server_count[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            # Zero-request servers = Total servers (n) - active servers in window
            res[q_idx] = n - active_servers
            
        return res