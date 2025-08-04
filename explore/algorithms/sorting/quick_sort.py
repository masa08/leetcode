from typing import List


def main():
    nums = [1, 8, 3, 9, 4, 5, 7]
    print(f"nums: {nums}")
    print(f"quick_sort: {quick_sort(nums)}")


def partition(numbers: List[int], low: int, high: int) -> int:
    pivot = numbers[high]
    store_index = low

    for i in range(low, high):
        if numbers[i] < pivot:
            numbers[store_index], numbers[i] = numbers[i], numbers[store_index]
            store_index += 1

    numbers[store_index], numbers[high] = numbers[high], numbers[store_index]

    return store_index


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index - 1)
            _quick_sort(numbers, partition_index + 1, high)

    _quick_sort(numbers, 0, len(numbers) - 1)
    return numbers


if __name__ == '__main__':
    main()
