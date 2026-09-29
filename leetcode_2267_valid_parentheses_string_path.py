class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        max_bal = (m + n - 1) // 2
        mask = (1 << (max_bal + 1)) - 1

        # dp[j] = bitmask of reachable balances at current row, column j
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prev = 1  # balance 0
                else:
                    prev = 0
                    if i > 0:
                        prev |= dp[j]        # from above
                    if j > 0:
                        prev |= dp[j - 1]    # from left
                if grid[i][j] == '(':
                    cur = (prev << 1) & mask
                else:
                    cur = prev >> 1          # drops balance; bit for -1 is discarded
                dp[j] = cur
        return (dp[n - 1] & 1) == 1