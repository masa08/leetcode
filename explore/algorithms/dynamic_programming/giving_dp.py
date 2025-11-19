"""
配るDP (Giving DP / Push DP)

【概念】
現在の状態が確定したら、その値を使って未来の状態に値を「配る」手法。
dp[i]が計算できたら、dp[i+1], dp[i+2]などに影響を与える。

【特徴】
- 遷移の方向が貰うDPと逆
- グラフの最短経路問題などで自然に適用できる場合がある
- 配る先の範囲チェックが必要

【パターン】
dp[i+k] += dp[i]  (i番目の値をi+k番目に配る)
"""

from typing import List


def fibonacci_giving(n: int) -> int:
    """
    フィボナッチ数を配るDPで求める

    dp[i] = i番目のフィボナッチ数
    i番目が確定したら、i+1番目とi+2番目に配る

    Time: O(n), Space: O(n)
    """
    if n < 2:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1  # 初期値

    for i in range(n):
        # i番目の値をi+1番目に「配る」
        dp[i + 1] += dp[i]

        # i番目の値をi+2番目に「配る」
        if i + 2 <= n:
            dp[i + 2] += dp[i]

    return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        LeetCode 70: Climbing Stairs (配るDPバージョン)

        【問題】
        階段をn段登る。1段または2段ずつ登れる。
        n段に到達する方法は何通りあるか？

        【考え方 - 配るDP】
        - i段目にいる時、i+1段目またはi+2段目に移動できる
        - dp[i] = i段目に到達する方法の数
        - i段目が確定したら、その値をi+1段目とi+2段目に「配る」

        Time: O(n), Space: O(n)
        """
        # Edge case
        if n <= 2:
            return n

        # dp[i]: i段目に到達する方法の数
        dp = [0] * (n + 1)

        # Base case: 0段目にいる状態からスタート
        dp[0] = 1  # 0段目にいる方法は1通り（スタート地点）

        # Fill DP table
        for i in range(n):
            if dp[i] == 0:  # この段に到達できない場合はスキップ
                continue

            # i段目からi+1段目に1段登る（dp[i]の値をdp[i+1]に配る）
            if i + 1 <= n:
                dp[i + 1] += dp[i]

            # i段目からi+2段目に2段登る（dp[i]の値をdp[i+2]に配る）
            if i + 2 <= n:
                dp[i + 2] += dp[i]

        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        LeetCode 746: Min Cost Climbing Stairs (配るDPバージョン)

        【問題】
        階段を登る際に各段でコストがかかる。
        0段目または1段目からスタートし、1段または2段ずつ登れる。
        頂上に到達する最小コストは？

        【考え方 - 配るDP】
        - i段目にいる時、cost[i]を支払ってi+1段目またはi+2段目に移動できる
        - dp[i] = i段目に到達する最小コスト
        - i段目が確定したら、cost[i]を支払ってi+1段目とi+2段目に値を「配る」

        Time: O(n), Space: O(n)
        """
        n = len(cost)

        # Edge case
        if n <= 2:
            return min(cost)

        # dp[i]: i段目に到達する最小コスト
        # n段目は頂上（コストなし）
        dp = [float('inf')] * (n + 1)

        # Base cases: 0段目と1段目からスタートできる（最初はコスト0）
        dp[0] = 0
        dp[1] = 0

        # Fill DP table
        for i in range(n):
            # i段目のコストを支払って、i+1段目に移動
            if i + 1 <= n:
                dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])

            # i段目のコストを支払って、i+2段目に移動
            if i + 2 <= n:
                dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])

        return dp[n]


def compare_dp_approaches():
    """
    貰うDPと配るDPの違いを視覚的に比較

    例: n=4の階段登り問題
    """
    print("=== 貰うDP vs 配るDP の比較 (n=4) ===\n")

    print("【貰うDP】")
    print("dp[i] = dp[i-1] + dp[i-2]  (過去から貰う)")
    print()
    print("  dp[0]=1 → ")
    print("  dp[1]=1 → ")
    print("  dp[2]=2 ← dp[1] + dp[0]")
    print("  dp[3]=3 ← dp[2] + dp[1]")
    print("  dp[4]=5 ← dp[3] + dp[2]")
    print()

    print("【配るDP】")
    print("dp[i+1] += dp[i], dp[i+2] += dp[i]  (未来に配る)")
    print()
    print("  dp[0]=1 → dp[1]+=1, dp[2]+=1")
    print("  dp[1]=1 → dp[2]+=1, dp[3]+=1")
    print("  dp[2]=2 → dp[3]+=2, dp[4]+=2")
    print("  dp[3]=3 → dp[4]+=3")
    print("  dp[4]=5")
    print()

    print("【どちらを使うべきか？】")
    print("✓ 貰うDP: 遷移式が明確で理解しやすい問題")
    print("✓ 配るDP: 遷移先が複数あったり、条件分岐が複雑な問題")
    print("✓ 多くの場合、貰うDPの方が直感的")
    print()


def main():
    solution = Solution()

    # Test: Climbing Stairs
    print("=== Climbing Stairs (配るDP) ===")
    test_cases_climb = [
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ]

    for n, expected in test_cases_climb:
        result = solution.climbStairs(n)
        assert result == expected, f"Failed for n={n}: got {result}, expected {expected}"
        print(f"n={n}: {result} ways ✓")

    # Test: Min Cost Climbing Stairs
    print("\n=== Min Cost Climbing Stairs (配るDP) ===")
    test_cases_cost = [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 99, 1], 6),
    ]

    for cost, expected in test_cases_cost:
        result = solution.minCostClimbingStairs(cost)
        assert result == expected, f"Failed for cost={cost}: got {result}, expected {expected}"
        print(f"cost={cost}: min_cost={result} ✓")

    # Test: Fibonacci
    print("\n=== Fibonacci (配るDP) ===")
    fib_tests = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ]

    for n, expected in fib_tests:
        result = fibonacci_giving(n)
        assert result == expected, f"Failed for n={n}: got {result}, expected {expected}"
        print(f"fib({n}) = {result} ✓")

    print("\n✅ All tests passed!")

    # 比較の可視化
    print("\n" + "=" * 50)
    compare_dp_approaches()


if __name__ == "__main__":
    main()
