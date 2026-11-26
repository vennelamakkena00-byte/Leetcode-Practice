class Solution:
    def canAliceWin(self, n):
        if n < 10:
            return False

        n -= 10
        stones = 9
        turn = 1  # Bob's turn

        while n >= stones:
            n -= stones
            stones -= 1
            turn += 1

        return turn % 2 == 1