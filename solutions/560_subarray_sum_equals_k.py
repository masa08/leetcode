from collections import defaultdict


def main():
    args = [1, 1, 1]
    solution = Solution()
    result = solution.subarraySum(args, 2)
    print(result)


class Solution:
    def subarraySum(self, nums, k):
        count, curr_sum = 0, 0
        sum_dict = defaultdict(int)
        sum_dict[0] = 1

        for i in range(len(nums)):
            curr_sum += nums[i]
            count += sum_dict[curr_sum-k]
            sum_dict[curr_sum] += 1

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
