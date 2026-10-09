class Solution:
    def minInsertions(self, s):
        insertions = 0
        balance = 0

        for ch in s:
            if ch == '(':
                balance += 2

                if balance % 2 == 1:
                    insertions += 1
                    balance -= 1
            else:
                balance -= 1

                if balance < 0:
                    insertions += 1
                    balance = 1

        return insertions + balance