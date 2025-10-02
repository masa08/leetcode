from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        result = []
        sorted_nums = sorted(nums)

        def backtrack(start_index, current_subset):
            """
            再帰の木構造イメージ (入力: [1, 2, 2] ソート済み)

            backtrack(0, [])
            ├─ [] を追加
            ├─ i=0: 1を選択 → backtrack(1, [1])
            │   ├─ [1] を追加
            │   ├─ i=1: 2を選択 → backtrack(2, [1,2])
            │   │   ├─ [1,2] を追加
            │   │   └─ i=2: 2を選択 → backtrack(3, [1,2,2])
            │   │       ├─ [1,2,2] を追加
            │   │       └─ (range(3,3)でループ終了)
            │   └─ i=2: 2を選択 (スキップ: i>1 and nums[2]==nums[1]) ✗
            ├─ i=1: 2を選択 → backtrack(2, [2])
            │   ├─ [2] を追加
            │   └─ i=2: 2を選択 → backtrack(3, [2,2])
            │       ├─ [2,2] を追加
            │       └─ (range(3,3)でループ終了)
            └─ i=2: 2を選択 (スキップ: i>0 and nums[2]==nums[1]) ✗

            結果: [[], [1], [1,2], [1,2,2], [2], [2,2]]

            重複回避のポイント:
            - 同じレベル(start_index)で同じ数字を2回選ばない
            - i > start_index: ループの2回目以降
            - nums[i] == nums[i-1]: 前と同じ数字
            """
            result.append(current_subset[:])

            for i in range(start_index, len(sorted_nums)):
                is_not_first_element = i > start_index
                is_same_as_previous = sorted_nums[i] == sorted_nums[i-1]
                is_duplicate_at_same_level = is_not_first_element and is_same_as_previous

                if is_duplicate_at_same_level:
                    continue

                current_subset.append(sorted_nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        backtrack(0, [])
        return result


def main():
    solution = Solution()

    # Basic cases
    assert sorted(solution.subsetsWithDup([1, 2, 2])) == sorted(
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    assert sorted(solution.subsetsWithDup([0])) == sorted([[], [0]])

    # Edge cases
    assert solution.subsetsWithDup([1]) == [[], [1]]
    assert sorted(solution.subsetsWithDup([1, 1])) == sorted([[], [1], [1, 1]])

    # Multiple duplicates
    # [], [1], [1,1], [1,1,1]
    assert len(solution.subsetsWithDup([1, 1, 1])) == 4

    print("All tests passed!")


if __name__ == "__main__":
    main()
