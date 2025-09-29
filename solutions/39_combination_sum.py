from typing import List


def main():
    solution = Solution()

    # テストケース1: 基本ケース
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    result1 = solution.combinationSum(candidates1, target1)
    assert sorted(result1) == sorted([[2, 2, 3], [7]])
    print(f"Test 1 passed: {result1}")

    # テストケース2: 複数の組み合わせ
    candidates2 = [2, 3, 5]
    target2 = 8
    result2 = solution.combinationSum(candidates2, target2)
    assert len(result2) == 3
    assert [2, 2, 2, 2] in result2
    assert [2, 3, 3] in result2
    assert [3, 5] in result2
    print(f"Test 2 passed: {len(result2)} combinations")

    # テストケース3: 単一要素のみ使用
    candidates3 = [2]
    target3 = 1
    result3 = solution.combinationSum(candidates3, target3)
    assert result3 == []
    print(f"Test 3 passed: no solution")

    # テストケース4: 単一要素の繰り返し
    candidates4 = [1]
    target4 = 2
    result4 = solution.combinationSum(candidates4, target4)
    assert result4 == [[1, 1]]
    print(f"Test 4 passed: single element repeated")

    # テストケース5: 要素が目標値と同じ
    candidates5 = [7, 3, 2]
    target5 = 7
    result5 = solution.combinationSum(candidates5, target5)
    assert [7] in result5
    assert [2, 2, 3] in result5 or [3, 2, 2] in result5
    print(f"Test 5 passed: exact match included")

    print("\n✓ All tests passed!")


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, comb, total):
            if total == target:
                ans.append(deepcopy(comb))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb, total + candidates[i])
                comb.pop()

        backtrack(0, [], 0)

        return ans


if __name__ == '__main__':
    main()
