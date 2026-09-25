class Solution(object):
    def braceExpansionII(self, expression):
        def parse(i):
            res = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    res |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    inside, i = parse(i + 1)

                    # Concatenate current × inside
                    current = {
                        a + b
                        for a in current
                        for b in inside
                    }

                else:
                    # Single lowercase letter
                    ch = expression[i]
                    current = {a + ch for a in current}
                    i += 1

            res |= current

            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return res, i

        result, _ = parse(0)

        return sorted(result)