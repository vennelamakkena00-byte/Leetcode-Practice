class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        both = min(need1, need2)

        if costBoth < cost1 + cost2:
            ans = both * costBoth
            need1 -= both
            need2 -= both
            ans += need1 * min(cost1, costBoth)
            ans += need2 * min(cost2, costBoth)
            return ans

        return need1 * cost1 + need2 * cost2