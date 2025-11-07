from typing import List


# TODO: ok/ngのイメージ
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Find first and last position of target using binary search.

        Approach:
        - Use binary search twice: once for leftmost, once for rightmost
        - ok/ng pattern for boundary search
        - Time: O(log n)
        - Space: O(1)
        """
        # Edge case
        if not nums:
            return [-1, -1]

        def findLeft(nums: List[int], target: int) -> int:
            """
            Lower Bound: nums[i] >= target となる最小のインデックス

            視覚化:
                nums = [5,7,7,8,8,10], target = 8
                cond:   F F F T T T  (nums[i] >= 8)
                        |-ng| |-ok-|
                              ↑ index 3
            """
            N = len(nums)

            # 範囲外チェック
            if target < nums[0] or target > nums[N - 1]:
                return -1

            # 最初の要素がtargetの場合
            if nums[0] == target:
                return 0

            # ok=N-1, ng=0から探索開始
            ok, ng = N - 1, 0
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if nums[mid] >= target:  # 条件: >=
                    ok = mid
                else:
                    ng = mid

            return ok if nums[ok] == target else -1

        def findRight(nums: List[int], target: int) -> int:
            """
            Upper Bound: nums[i] <= target となる最大のインデックス

            視覚化:
                nums = [5,7,7,8,8,10], target = 8
                cond:   T T T T T F  (nums[i] <= 8)
                        |---ok--| |ng|
                                  ↑ index 4
            """
            N = len(nums)

            # 範囲外チェック
            if target < nums[0] or target > nums[N - 1]:
                return -1

            # 最後の要素がtargetの場合
            if nums[N - 1] == target:
                return N - 1

            # ok=0, ng=N-1から探索開始
            ok, ng = 0, N - 1
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if nums[mid] <= target:  # 条件: <=
                    ok = mid
                else:
                    ng = mid

            return ok if nums[ok] == target else -1

        left_pos = findLeft(nums, target)

        # If target not found, return [-1, -1]
        if left_pos == -1:
            return [-1, -1]

        right_pos = findRight(nums, target)

        return [left_pos, right_pos]


def main():
    solution = Solution()

    # Basic cases
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

    # Edge cases
    assert solution.searchRange([], 0) == [-1, -1]
    assert solution.searchRange([1], 1) == [0, 0]
    assert solution.searchRange([1], 2) == [-1, -1]

    # Single occurrence
    assert solution.searchRange([1, 2, 3, 4, 5], 3) == [2, 2]

    # All same elements
    assert solution.searchRange([5, 5, 5, 5, 5], 5) == [0, 4]

    # Target at boundaries
    assert solution.searchRange([1, 2, 3, 4, 5], 1) == [0, 0]
    assert solution.searchRange([1, 2, 3, 4, 5], 5) == [4, 4]

    print("All tests passed!")


if __name__ == "__main__":
    main()
