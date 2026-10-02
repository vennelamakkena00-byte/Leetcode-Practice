class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(s, open_count, close_count):
            # If the string has 2*n characters, it is complete
            if len(s) == 2 * n:
                result.append(s)
                return

            # Add '(' if we still have opening brackets available
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # Add ')' only if it won't make the string invalid
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result