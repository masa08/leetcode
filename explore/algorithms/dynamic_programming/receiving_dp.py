"""
貰うDP (Receiving DP / Pull DP)

【概念】
現在の状態を求めるために、既に計算済みの過去の状態から値を「貰って」計算する手法。
dp[i]を計算する際に、dp[i-1], dp[i-2]など過去の値を参照する。

【特徴】
- 直感的で理解しやすい
- 遷移式がシンプルに書ける
- 多くの問題で自然に適用できる

【パターン】
dp[i] = f(dp[i-1], dp[i-2], ...)
"""

from typing import List


def fibonacci_receiving(n: int) -> int:
    """
    フィボナッチ数を貰うDPで求める

    dp[i] = i番目のフィボナッチ数
    遷移式: dp[i] = dp[i-1] + dp[i-2]

    Time: O(n), Space: O(n)
    """
    if n < 2:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        # i番目を求めるために、i-1番目とi-2番目の値を「貰う」
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        LeetCode 70: Climbing Stairs

        【問題】
        階段をn段登る。1段または2段ずつ登れる。
        n段に到達する方法は何通りあるか？

        【考え方】
        - n段目に到達するには、(n-1)段目から1段登るか、(n-2)段目から2段登るかの2通り
        - dp[i] = i段目に到達する方法の数
        - 遷移式: dp[i] = dp[i-1] + dp[i-2]

        【貰うDP】
        i段目の値を求める際に、i-1段目とi-2段目の値を「貰って」計算する

        Time: O(n), Space: O(n)
        """
        # Edge case
        if n <= 2:
            return n

        # dp[i]: i段目に到達する方法の数
        dp = [0] * (n + 1)

        # Base cases
        dp[1] = 1  # 1段目: 1通り
        dp[2] = 2  # 2段目: 2通り (1+1 or 2)

        # Fill DP table
        for i in range(3, n + 1):
            # i段目は (i-1)段目と(i-2)段目の値を貰って計算
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairs_optimized(self, n: int) -> int:
        """
        Space complexity最適化版: O(1)

        直前の2つの値だけを保持すれば良い
        """
        if n <= 2:
            return n

        # 1つ前と2つ前の値を保持
        prev1, prev2 = 2, 1  # dp[2], dp[1]

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        LeetCode 746: Min Cost Climbing Stairs

        【問題】
        階段を登る際に各段でコストがかかる。
        0段目または1段目からスタートし、1段または2段ずつ登れる。
        頂上に到達する最小コストは？

        【考え方】
        - i段目に到達する最小コストを求める
        - dp[i] = i段目に到達する最小コスト
        - 遷移式: dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        【貰うDP】
        i段目の最小コストを求める際に、i-1段目とi-2段目の最小コストを「貰って」計算

        Time: O(n), Space: O(n)
        """
        n = len(cost)

        # Edge case
        if n <= 2:
            return min(cost)

        # dp[i]: i段目に到達する最小コスト
        dp = [0] * n

        # Base cases: 0段目と1段目からスタートできる
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Fill DP table
        for i in range(2, n):
            # i段目のコストを求めるために、i-1段目とi-2段目の最小コストを貰う
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # 最後の段に到達せずに頂上に行ける（最後から1段 or 2段ジャンプ）
        return min(dp[n - 1], dp[n - 2])

    def minCostClimbingStairs_optimized(self, cost: List[int]) -> int:
        """
        Space complexity最適化版: O(1)
        """
        n = len(cost)
        if n <= 2:
            return min(cost)

        # 1つ前と2つ前の最小コストを保持
        prev1, prev2 = cost[1], cost[0]

        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current

        return min(prev1, prev2)


def main():
    solution = Solution()

    # Test: Climbing Stairs
    print("=== Climbing Stairs ===")
    test_cases_climb = [
        (2, 2),   # 1+1, 2
        (3, 3),   # 1+1+1, 1+2, 2+1
        (4, 5),   # 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2
        (5, 8),
    ]

    for n, expected in test_cases_climb:
        result = solution.climbStairs(n)
        result_opt = solution.climbStairs_optimized(n)
        assert result == expected, f"Failed for n={n}: got {result}, expected {expected}"
        assert result_opt == expected, f"Failed optimized for n={n}: got {result_opt}, expected {expected}"
        print(f"n={n}: {result} ways ✓")

    # Test: Min Cost Climbing Stairs
    print("\n=== Min Cost Climbing Stairs ===")
    test_cases_cost = [
        ([10, 15, 20], 15),                    # Start at 1, pay 15
        ([1, 100, 1, 1, 1, 100, 1, 1, 99, 1], 6),  # 1+1+1+1+1+1
    ]

    for cost, expected in test_cases_cost:
        result = solution.minCostClimbingStairs(cost)
        result_opt = solution.minCostClimbingStairs_optimized(cost)
        assert result == expected, f"Failed for cost={cost}: got {result}, expected {expected}"
        assert result_opt == expected, f"Failed optimized for cost={cost}: got {result_opt}, expected {expected}"
        print(f"cost={cost}: min_cost={result} ✓")

    # Test: Fibonacci
    print("\n=== Fibonacci (Receiving DP) ===")
    fib_tests = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ]

    for n, expected in fib_tests:
        result = fibonacci_receiving(n)
        assert result == expected, f"Failed for n={n}: got {result}, expected {expected}"
        print(f"fib({n}) = {result} ✓")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    main()
