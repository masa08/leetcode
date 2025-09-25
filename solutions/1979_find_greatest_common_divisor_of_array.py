from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        """
        配列の最小値と最大値の最大公約数を返す

        Time: O(n + log(min(a,b))) - n for finding min/max, log for GCD
        Space: O(1)
        """
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        min_num = min(nums)
        max_num = max(nums)

        return gcd(min_num, max_num)


def main():
    solution = Solution()

    # 基本ケース
    nums1 = [2, 5, 6, 9, 10]
    assert solution.findGCD(
        nums1) == 2, f"Expected 2, got {solution.findGCD(nums1)}"

    nums2 = [7, 5, 6, 8, 3]
    assert solution.findGCD(
        nums2) == 1, f"Expected 1, got {solution.findGCD(nums2)}"

    nums3 = [3, 3]
    assert solution.findGCD(
        nums3) == 3, f"Expected 3, got {solution.findGCD(nums3)}"

    # エッジケース
    # 単一要素
    nums4 = [5]
    assert solution.findGCD(
        nums4) == 5, f"Expected 5, got {solution.findGCD(nums4)}"

    # 2要素
    nums5 = [4, 8]
    assert solution.findGCD(
        nums5) == 4, f"Expected 4, got {solution.findGCD(nums5)}"

    # 大きな値
    nums6 = [100, 200]
    assert solution.findGCD(
        nums6) == 100, f"Expected 100, got {solution.findGCD(nums6)}"

    # 素数同士
    nums7 = [2, 3, 5, 7, 11]
    assert solution.findGCD(
        nums7) == 1, f"Expected 1, got {solution.findGCD(nums7)}"

    # 最小値と最大値が同じ倍数関係
    nums8 = [6, 12, 18, 24]
    assert solution.findGCD(
        nums8) == 6, f"Expected 6, got {solution.findGCD(nums8)}"

    # 公約数が2以上
    nums9 = [14, 21, 28, 35]
    assert solution.findGCD(
        nums9) == 7, f"Expected 7, got {solution.findGCD(nums9)}"

    # 連続する数値
    nums10 = [10, 11, 12, 13, 14]
    assert solution.findGCD(
        nums10) == 2, f"Expected 2, got {solution.findGCD(nums10)}"

    print("All tests passed!")


if __name__ == "__main__":
    main()
