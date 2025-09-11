from collections import defaultdict


def main():
    solution = Solution()

    # 基本ケース
    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2
    
    # エッジケース
    assert solution.subarraySum([1], 1) == 1  # 単一要素
    assert solution.subarraySum([1], 0) == 0  # 単一要素、和が異なる
    assert solution.subarraySum([], 0) == 0   # 空配列
    
    # 特殊ケース
    assert solution.subarraySum([0, 0], 0) == 3  # ゼロの配列
    assert solution.subarraySum([-1, -1, 1], 0) == 1  # 負の数を含む
    
    print("All tests passed!")


class Solution:
    def subarraySum(self, nums, k):
        """
        累積和とハッシュマップを使って部分配列の和がkになる個数を数える

        キーアイデア:
        部分配列[i, j]の和 = prefix_sum[j] - prefix_sum[i-1] = k
        つまり: prefix_sum[j] - k = prefix_sum[i-1]

        現在の累積和からkを引いた値が過去に出現した回数が、
        現在位置で終わる和がkの部分配列の個数になる
        """
        from collections import defaultdict

        count, cur_prefix_sum = 0, 0
        # 各累積和が何回出現したかを記録
        prefix_sum_counter = defaultdict(int)
        # 空の部分配列を表す（最初から現在までの和がkの場合に必要）
        prefix_sum_counter[0] = 1

        for num in nums:
            # 現在位置までの累積和を計算
            cur_prefix_sum += num

            # 「現在の累積和 - k」が過去に出現していれば、
            # その位置から現在位置までの部分配列の和がkになる
            if cur_prefix_sum - k in prefix_sum_counter:
                count += prefix_sum_counter[cur_prefix_sum - k]

            # 現在の累積和を記録（将来の計算で使用）
            prefix_sum_counter[cur_prefix_sum] += 1

        return count

        # count = current_sum = 0
        # h = defaultdict(int)

        # for num in nums:
        #     current_sum += num

        #     # 最初からnumまでの合計和がkの場合
        #     if current_sum == k:
        #         count += 1

        #     # 部分配列の和がkの場合
        #     count += h[current_sum-k]

        #     # すでに出現したcurrent_sumの回数をカウント
        #     h[current_sum] += 1

        # return count


if __name__ == '__main__':
    main()
