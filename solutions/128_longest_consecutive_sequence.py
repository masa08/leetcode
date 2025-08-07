from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

    # エッジケース
    assert solution.longestConsecutive([]) == 0
    assert solution.longestConsecutive([1]) == 1
    assert solution.longestConsecutive([1, 1, 1]) == 1

    # 負の数を含む
    assert solution.longestConsecutive([-1, -2, 0, 1, 2]) == 5
    assert solution.longestConsecutive([-5, -4, -3, -2, -1]) == 5

    # 飛び飛びの数値
    assert solution.longestConsecutive([1, 3, 5, 7, 9]) == 1
    assert solution.longestConsecutive([10, 20, 30, 40]) == 1

    print("All tests passed!")


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_consecutive_length, num_set = 0, set(nums)

        for num in nums:
            if num not in num_set:
                continue

            num_set.remove(num)
            current_consecutive_length = 1

            i = 1
            while num + i in num_set:
                num_set.remove(num+i)
                current_consecutive_length += 1
                i += 1

            j = 1
            while num - j in num_set:
                num_set.remove(num-j)
                current_consecutive_length += 1
                j += 1

            max_consecutive_length = max(
                max_consecutive_length, current_consecutive_length)

        return max_consecutive_length

    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        cur_consecutive_length = max_consecutive_length = 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue

            if nums[i-1] + 1 == nums[i]:
                cur_consecutive_length += 1
                max_consecutive_length = max(
                    cur_consecutive_length,
                    max_consecutive_length
                )
            else:
                cur_consecutive_length = 1
        return max_consecutive_length


if __name__ == '__main__':
    main()
