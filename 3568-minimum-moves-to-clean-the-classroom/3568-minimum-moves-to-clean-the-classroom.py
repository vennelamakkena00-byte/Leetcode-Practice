from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_index = {}
        litter_count = 0

        # Find start and assign each litter a bit index
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)

                elif classroom[r][c] == 'L':
                    litter_index[(r, c)] = litter_count
                    litter_count += 1

        # No litter
        if litter_count == 0:
            return 0

        target_mask = (1 << litter_count) - 1

        # best[r][c][mask] = maximum energy remaining
        best = [[[-1] * (1 << litter_count) for _ in range(n)]
                for _ in range(m)]

        sr, sc = start

        queue = deque()
        queue.append((sr, sc, 0, energy, 0))

        best[sr][sc][0] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c, mask, remaining, moves = queue.popleft()

            if mask == target_mask:
                return moves

            # Cannot make another move
            if remaining == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Invalid position
                if (
                    nr < 0 or nr >= m or
                    nc < 0 or nc >= n or
                    classroom[nr][nc] == 'X'
                ):
                    continue

                new_remaining = remaining - 1
                new_mask = mask

                cell = classroom[nr][nc]

                # Collect litter
                if cell == 'L':
                    new_mask |= (1 << litter_index[(nr, nc)])

                # Reset energy
                if cell == 'R':
                    new_remaining = energy

                # If we already reached this position + mask
                # with equal or more energy, skip it
                if best[nr][nc][new_mask] >= new_remaining:
                    continue

                best[nr][nc][new_mask] = new_remaining
                queue.append(
                    (nr, nc, new_mask, new_remaining, moves + 1)
                )

        return -1