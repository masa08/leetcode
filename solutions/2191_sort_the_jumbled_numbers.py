from typing import List


def main():
    solution = Solution()

    # Test Case 1: Example 1
    mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    nums = [991, 338, 38]
    result = solution.sortJumbled(mapping, nums)
    assert result == [338, 38, 991], f"Test 1 failed: {result}"

    # Test Case 2: Example 2
    mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = [789, 456, 123]
    result = solution.sortJumbled(mapping, nums)
    assert result == [123, 456, 789], f"Test 2 failed: {result}"

    print("All tests passed!")


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped(num: int):
            if num == 0:
                return mapping[0]

            mapped_number = 0
            factor = 1
            while num > 0:
                digit = num % 10
                mapped_digit = mapping[digit]
                mapped_number += mapped_digit * factor
                factor *= 10
                num = num // 10
            return mapped_number

        nums.sort(key=get_mapped)
        return nums


if __name__ == '__main__':
    main()
