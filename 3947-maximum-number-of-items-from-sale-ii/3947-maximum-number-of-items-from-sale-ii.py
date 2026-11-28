class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)

        freq = [0] * (n + 1)
        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        count = [0] * (n + 1)

        for factor in range(1, n + 1):
            for multiple in range(factor, n + 1, factor):
                count[factor] += freq[multiple]

        deals = []

        for factor, price in items:
            free_count = count[factor] - 1

            if free_count > 0 and price < 2 * min_price:
                deals.append((price, free_count))

        deals.sort()

        answer = 0

        for price, free_count in deals:
            if budget < price:
                break

            take = min(free_count, budget // price)

            answer += take * 2
            budget -= take * price

        answer += budget // min_price

        return answer