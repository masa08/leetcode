from typing import List


def main():
    solution = Solution()

    # Test case 1: Basic case
    assert solution.majorityElement([3, 2, 3]) == 3

    # Test case 2: All same elements
    assert solution.majorityElement([1, 1, 1, 1]) == 1

    # Test case 3: Single element
    assert solution.majorityElement([1]) == 1

    print("All tests passed!")


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Find majority element using Hash Map

        Algorithm:
        1. Count occurrences of each element using Hash Map
        2. Return element with count >= n/2

        Time Complexity: O(n) - traverse array twice
        Space Complexity: O(n) - store up to n elements in Hash Map
        """
        # Calculate threshold for majority element
        pivod = len(nums)/2
        # Hash map to store element counts
        counter = {}

        # Count occurrences of each element
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1

        # Find and return element with count >= threshold
        for i, v in counter.items():
            if v >= pivod:
                return i


if __name__ == '__main__':
    main()
