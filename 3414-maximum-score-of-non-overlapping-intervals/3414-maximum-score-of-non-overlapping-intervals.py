from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # [left, right, weight, original_index]
        arr = []
        for i in range(n):
            l, r, w = intervals[i]
            arr.append((l, r, w, i))

        # Sort by left endpoint
        arr.sort()

        starts = [x[0] for x in arr]

        # next interval must have left > current right
        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = (maximum score, lexicographically smallest indices)
        # using intervals from i onward, choosing at most k intervals.
        dp = [[None] * 5 for _ in range(n + 1)]

        # Choosing at most 0 intervals gives score 0 and empty list.
        for i in range(n + 1):
            dp[i][0] = (0, ())

        # Base case: no intervals left
        for k in range(1, 5):
            dp[n][k] = (0, ())

        # Fill DP backwards
        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                # Don't take this interval
                skip_score, skip_indices = dp[i + 1][k]

                # Take this interval
                take_score_next, take_indices_next = dp[nxt[i]][k - 1]

                take_score = arr[i][2] + take_score_next
                take_indices = tuple(
                    sorted((arr[i][3],) + take_indices_next)
                )

                # Select the better choice
                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)

                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)

                else:
                    # Same score → lexicographically smaller indices
                    if take_indices < skip_indices:
                        dp[i][k] = (take_score, take_indices)
                    else:
                        dp[i][k] = (skip_score, skip_indices)

        return list(dp[0][4][1])