from typing import List


def main():
    test_cases = [
        [],
        [1],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [5, 4, 3, 2, 1]
    ]

    for nums in test_cases:
        print(f"\n元の配列: {nums}")
        print(f"ソート後: {merge_sort(nums)}")


def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == '__main__':
    main()
