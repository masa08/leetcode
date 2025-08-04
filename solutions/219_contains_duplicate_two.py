from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
    assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False

    # エッジケース
    assert solution.containsNearbyDuplicate([], 0) == False
    assert solution.containsNearbyDuplicate([1], 1) == False
    assert solution.containsNearbyDuplicate([1, 2], 0) == False

    print("All tests passed!")


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             if abs(i-j) <= k:
        #                 return True
        # return False

        mapping = {}
        for i, num in enumerate(nums):
            if num in mapping:
                if abs(i - mapping[num]) <= k:
                    return True
            mapping[num] = i

        return False


if __name__ == '__main__':
    main()
