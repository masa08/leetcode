from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    # ゼロを含むケース
    assert solution.productExceptSelf([0, 1, 2]) == [2, 0, 0]

    # エッジケース
    assert solution.productExceptSelf([1, 1]) == [1, 1]

    print("All tests passed!")


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        アプローチ: Prefix/Suffix積の分離計算

        1. left[i] = nums[0] * nums[1] * ... * nums[i-1] (i番目より左の全要素の積)
        2. right[i] = nums[i+1] * nums[i+2] * ... * nums[n-1] (i番目より右の全要素の積)
        3. answer[i] = left[i] * right[i]

        例: nums = [1,2,3,4]
        - left = [1, 1, 2, 6]  (左側の累積積)
        - right = [24, 12, 4, 1]  (右側の累積積)
        - answer = [24, 12, 8, 6]

        時間計算量: O(n) - 3回の線形走査
        空間計算量: O(n) - 3つの配列を使用
        """
        length = len(nums)
        left, right, answer = [1] * length, [1] * length, [1] * length

        for i in range(1, length):
            left[i] = nums[i-1] * left[i-1]

        for i in reversed(range(length-1)):
            right[i] = nums[i+1] * right[i+1]

        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer

        # length = len(nums)
        # answer = [1] * length
        # for i in range(1, length):
        #     answer[i] = nums[i-1] * answer[i-1]

        # r = 1
        # for i in reversed(range(length)):
        #     answer[i] = answer[i] * r
        #     r *= nums[i]

        # return answer


if __name__ == '__main__':
    main()
