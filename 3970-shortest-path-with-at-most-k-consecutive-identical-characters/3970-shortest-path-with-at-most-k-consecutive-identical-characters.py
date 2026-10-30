import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        pq = [(0, 0, 1)]
        
        dist = {(0, 1): 0}

        while pq:
            cost, node, count = heapq.heappop(pq)

            if cost != dist.get((node, count), float('inf')):
                continue

            if node == n - 1:
                return cost

            for nei, w in graph[node]:
                if labels[nei] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + w
                state = (nei, new_count)

                if new_cost < dist.get(state, float('inf')):
                    dist[state] = new_cost
                    heapq.heappush(pq, (new_cost, nei, new_count))

        return -1