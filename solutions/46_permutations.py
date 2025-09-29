from typing import List


def main():
    """
    LeetCode 46: Permutations
    順列を生成する問題の基本テストケース
    """
    solution = Solution()

    # テストケース1: 基本的な3要素
    nums1 = [1, 2, 3]
    result1 = solution.permute(nums1)
    assert len(result1) == 6
    assert [1, 2, 3] in result1
    assert [3, 2, 1] in result1
    print(f"Test 1 passed: {len(result1)} permutations")

    # テストケース2: 単一要素
    nums2 = [1]
    result2 = solution.permute(nums2)
    assert result2 == [[1]]
    print(f"Test 2 passed: single element")

    # テストケース3: 2要素
    nums3 = [1, 2]
    result3 = solution.permute(nums3)
    assert len(result3) == 2
    assert sorted(result3) == [[1, 2], [2, 1]]
    print(f"Test 3 passed: 2 permutations")

    # テストケース4: 重複なしの確認
    nums4 = [1, 2, 3, 4]
    result4 = solution.permute(nums4)
    assert len(result4) == 24
    assert len(set(map(tuple, result4))) == 24  # 全て異なる順列
    print(f"Test 4 passed: {len(result4)} unique permutations")

    print("\n✓ All tests passed!")


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums[:]]

        result = []
        self._build_permutation(
            nums,
            current_path=[],
            used_indices=set(),
            result=result
        )
        return result

    def _build_permutation(self, nums, current_path, used_indices, result):
        if len(current_path) == len(nums):
            result.append(current_path[:])
            return

        for i in range(len(nums)):
            if i in used_indices:
                continue

            used_indices.add(i)
            current_path.append(nums[i])

            self._build_permutation(nums, current_path, used_indices, result)

            current_path.pop()
            used_indices.remove(i)


if __name__ == '__main__':
    main()
