class Solution:
    def totalNumbers(self, digits):
        count = 0

        for num in range(100, 1000):
            # Must be even
            if num % 2 != 0:
                continue

            # Get the three digits
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Count how many times each digit is needed
            needed = [0] * 10
            needed[a] += 1
            needed[b] += 1
            needed[c] += 1

            # Count available digits
            available = [0] * 10
            for d in digits:
                available[d] += 1

            # Check if we have enough copies
            possible = True
            for d in range(10):
                if needed[d] > available[d]:
                    possible = False
                    break

            if possible:
                count += 1

        return count