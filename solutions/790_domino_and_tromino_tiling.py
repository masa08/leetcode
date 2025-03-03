def main():
    args = 3
    solution = Solution()
    result = solution.numTilings(args)
    print(result)


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp = [0] * (n+1)
        sum_dp = [0] * (n+1)

        dp[0], dp[1], dp[2] = 1, 1, 2
        sum_dp[0], sum_dp[1], sum_dp[2] = 1, 2, 4

        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2] + (2 * sum_dp[i-3])) % MOD
            sum_dp[i] = (sum_dp[i-1] + dp[i]) % MOD

        return dp[n]


if __name__ == '__main__':
    main()
