from collections import defaultdict


def main():
    args = [1, 1, 1]
    solution = Solution()
    result = solution.subarraySum(args, 2)
    print(result)


class Solution:
    def subarraySum(self, nums, k):
        count = current_sum = 0
        h = defaultdict(int)

        for num in nums:
            current_sum += num

            # 最初からnumまでの合計和がkの場合
            if current_sum == k:
                count += 1

            # 部分配列の和がkの場合
            count += h[current_sum-k]

            # すでに出現したcurrent_sumの回数をカウント
            h[current_sum] += 1

        return count


if __name__ == '__main__':
    main()
