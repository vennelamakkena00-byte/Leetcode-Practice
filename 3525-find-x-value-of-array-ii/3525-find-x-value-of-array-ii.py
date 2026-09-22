class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = [[1, [0] * k] for _ in range(4 * n)]

        def make_leaf(value):
            value %= k
            pref = [0] * k
            pref[value] = 1
            return [value, pref]

        def merge(left, right):
            left_prod, left_pref = left
            right_prod, right_pref = right

            prod = (left_prod * right_prod) % k
            pref = left_pref[:]

            for x in range(k):
                new_rem = (left_prod * x) % k
                pref[new_rem] += right_pref[x]

            return [prod, pref]

        def build(node, l, r):
            if l == r:
                tree[node] = make_leaf(nums[l])
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                tree[node] = make_leaf(value)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:

            # Persistent update
            nums[index] = value
            update(1, 0, n - 1, index, value)

            # Count prefix products of nums[start:]
            _, pref = query(
                1, 0, n - 1,
                start,
                n - 1
            )

            result.append(pref[x])

        return result