from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.canJump([2, 3, 1, 1, 4]) is True
    assert solution.canJump([3, 2, 1, 0, 4]) is False

    # Edge cases
    assert solution.canJump([0]) is True       # Already at the end
    assert solution.canJump([2, 0]) is True    # Can jump over 0
    assert solution.canJump([0, 1]) is False   # Stuck at index 0

    print("All tests passed!")


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy: track the farthest reachable index.
        At each position, update max_reach. If current index exceeds
        max_reach, we can never get here — return False.

        Time: O(n) - single pass
        Space: O(1) - one variable
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

        return True


if __name__ == '__main__':
    main()
