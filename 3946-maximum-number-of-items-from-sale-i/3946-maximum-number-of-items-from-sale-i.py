class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)

        factors = [x[0] for x in items]
        prices = [x[1] for x in items]

        # Number of copies obtained by activating each item type.
        values = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j and factors[j] % factors[i] == 0:
                    values[i] += 1

        groups = {}

        for i in range(n):
            if prices[i] <= budget:
                groups.setdefault(prices[i], []).append(i)

        INF = float('-inf')

        # dp[c] = maximum activation value with exact cost c.
        dp = [INF] * (budget + 1)
        dp[0] = 0

        answer = 0

        # Process prices from largest to smallest.
        for p in sorted(groups.keys(), reverse=True):

            # States with no item of price p activated.
            none = dp[:]

            # States with at least one item of price p activated.
            has = [INF] * (budget + 1)

            for idx in groups[p]:
                cost = p
                val = values[idx]

                for c in range(budget, cost - 1, -1):

                    # Activate this item as the first item of price p.
                    if none[c - cost] != INF:
                        has[c] = max(
                            has[c],
                            none[c - cost] + val
                        )

                    # Activate another item of price p.
                    if has[c - cost] != INF:
                        has[c] = max(
                            has[c],
                            has[c - cost] + val
                        )

            # At least one item of price p must be activated.
            for c in range(budget + 1):
                if has[c] != INF:
                    total = has[c] + (budget - c) // p
                    answer = max(answer, total)

            # Update DP for the next smaller price.
            for c in range(budget + 1):
                dp[c] = max(dp[c], has[c])

        return answer