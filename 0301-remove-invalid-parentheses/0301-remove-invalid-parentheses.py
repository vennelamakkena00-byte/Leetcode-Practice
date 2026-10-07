from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = set([s])
        answer = []
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                answer.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] != '(' and current[i] != ')':
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return answer