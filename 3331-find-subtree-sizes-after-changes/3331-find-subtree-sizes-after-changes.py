class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Build the modified tree
        new_children = [[] for _ in range(n)]

        last = [-1] * 26

        stack = [(0, 0, -1)]

        while stack:
            node, state, prev = stack.pop()

            idx = ord(s[node]) - ord('a')

            if state == 0:
                # Find the closest ancestor with the same character
                new_parent = last[idx]

                if new_parent == -1:
                    new_parent = parent[node]

                if node != 0:
                    new_children[new_parent].append(node)

                # Save previous occurrence
                prev = last[idx]
                last[idx] = node

                # Exit event
                stack.append((node, 1, prev))

                # Visit original children
                for child in reversed(children[node]):
                    stack.append((child, 0, -1))

            else:
                # Restore previous occurrence
                last[idx] = prev

        # Calculate subtree sizes in the modified tree
        answer = [1] * n

        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        # Process children before parents
        for node in reversed(order):
            for child in new_children[node]:
                answer[node] += answer[child]

        return answer