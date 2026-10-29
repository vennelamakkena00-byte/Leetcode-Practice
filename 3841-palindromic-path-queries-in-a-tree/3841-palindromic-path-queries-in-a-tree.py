class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        for u in reversed(order):
            p = parent[u]
            if p != -1:
                size[p] += size[u]
        for u in order:
            best = 0
            for v in adj[u]:
                if v != parent[u] and size[v] > best:
                    best = size[v]
                    heavy[u] = v

        head = [0] * n
        pos = [0] * n
        cur = 0
        for u in order:
            if parent[u] == -1 or heavy[parent[u]] != u:
                v = u
                while v != -1:
                    head[v] = u
                    pos[v] = cur
                    cur += 1
                    v = heavy[v]

        seg = 1
        while seg < n:
            seg <<= 1
        tree = [0] * (2 * seg)
        for i in range(n):
            tree[seg + pos[i]] = 1 << (ord(s[i]) - 97)
        for i in range(seg - 1, 0, -1):
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]

        def update(i, val):
            i += seg
            tree[i] = val
            i >>= 1
            while i:
                tree[i] = tree[2 * i] ^ tree[2 * i + 1]
                i >>= 1

        def range_xor(l, r):
            res = 0
            l += seg
            r += seg + 1
            while l < r:
                if l & 1:
                    res ^= tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= tree[r]
                l >>= 1
                r >>= 1
            return res

        def path_xor(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= range_xor(pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                update(pos[int(parts[1])], 1 << (ord(parts[2]) - 97))
            else:
                m = path_xor(int(parts[1]), int(parts[2]))
                ans.append((m & (m - 1)) == 0)
        return ans