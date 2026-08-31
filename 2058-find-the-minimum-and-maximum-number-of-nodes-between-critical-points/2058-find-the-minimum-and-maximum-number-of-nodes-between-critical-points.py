class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        pos = 1

        first = -1
        last = -1
        minDist = float('inf')

        while curr.next:
            next_node = curr.next
            pos += 1

            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    minDist = min(minDist, pos - last)

                last = pos

            prev = curr
            curr = next_node

        # Fewer than two critical points
        if first == -1 or first == last:
            return [-1, -1]

        maxDist = last - first

        return [minDist, maxDist]