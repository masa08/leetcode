from typing import List


def main():
    solution = Solution()

    # 基本ケース
    nums1 = [3, 2, 2, 3]
    assert solution.removeElement(nums1, 3) == 2
    assert nums1[:2] == [2, 2]  # 最初の2要素が残存要素

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    assert solution.removeElement(nums2, 2) == 5
    assert sorted(nums2[:5]) == [0, 0, 1, 3, 4]  # 削除対象以外の要素

    # エッジケース
    nums3 = []
    assert solution.removeElement(nums3, 1) == 0  # 空配列

    nums4 = [1]
    assert solution.removeElement(nums4, 1) == 0  # 全要素削除

    nums5 = [1]
    assert solution.removeElement(nums5, 2) == 1  # 削除対象なし

    print("All tests passed!")


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return slow


if __name__ == '__main__':
    main()
