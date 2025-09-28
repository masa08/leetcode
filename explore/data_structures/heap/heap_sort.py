from typing import List


class MaxHeap:
    @staticmethod
    def parent(i: int) -> int:
        return (i - 1) // 2

    @staticmethod
    def left_child(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def right_child(i: int) -> int:
        return 2 * i + 2

    @staticmethod
    def push(heap: List[int], value: int) -> None:
        heap.append(value)
        MaxHeap._bubble_up(heap, len(heap) - 1)

    @staticmethod
    def pop(heap: List[int]) -> int:
        if not heap:
            raise IndexError("pop from empty heap")
        max_val = heap[0]
        if len(heap) == 1:
            heap.pop()
        else:
            heap[0] = heap.pop()
            MaxHeap._sift_down(heap, 0, len(heap))
        return max_val

    @staticmethod
    def heapify(arr: List[int]) -> None:
        for i in range(len(arr) // 2 - 1, -1, -1):
            MaxHeap._sift_down(arr, i, len(arr))

    @staticmethod
    def _bubble_up(heap: List[int], idx: int) -> None:
        while idx > 0:
            parent_idx = MaxHeap.parent(idx)
            if heap[idx] > heap[parent_idx]:
                heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
                idx = parent_idx
            else:
                break

    @staticmethod
    def _sift_down(arr: List[int], idx: int, size: int) -> None:
        while True:
            left = MaxHeap.left_child(idx)
            right = MaxHeap.right_child(idx)
            largest = idx

            if left < size and arr[left] > arr[largest]:
                largest = left
            if right < size and arr[right] > arr[largest]:
                largest = right

            if largest == idx:
                break

            arr[idx], arr[largest] = arr[largest], arr[idx]
            idx = largest


def heap_sort(arr: List[int]) -> None:
    """Heap sort implementation - O(n log n) time, O(1) space"""
    if len(arr) <= 1:
        return

    MaxHeap.heapify(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        MaxHeap._sift_down(arr, 0, i)


def _verify_heap(heap: List[int]) -> None:
    """Verify max heap property"""
    for i in range(len(heap) // 2):
        left = MaxHeap.left_child(i)
        right = MaxHeap.right_child(i)
        assert left >= len(heap) or heap[i] >= heap[left]
        assert right >= len(heap) or heap[i] >= heap[right]


def test_heap_operations():
    print("\n=== Testing MaxHeap ===")

    # Test push and pop
    heap = []
    values = [3, 1, 4, 1, 5, 9, 2, 6]

    for val in values:
        MaxHeap.push(heap, val)
        _verify_heap(heap)

    popped = []
    while heap:
        popped.append(MaxHeap.pop(heap))
        _verify_heap(heap)

    assert popped == sorted(values, reverse=True)

    # Test heapify
    arr = [1, 5, 8, 0, 2, 6, 3, 9, 10, 4, 7, 11]
    MaxHeap.heapify(arr)
    _verify_heap(arr)

    # Edge cases
    try:
        MaxHeap.pop([])
        assert False
    except IndexError:
        pass

    heap = []
    MaxHeap.push(heap, 42)
    assert MaxHeap.pop(heap) == 42
    assert heap == []

    print("✓ All heap tests passed")


def test_heap_sort():
    print("\n=== Testing Heap Sort ===")

    test_cases = [
        ([7, 3, 2, 5, 6, 10, 9, 8, 1], "random"),
        ([3, 1, 4, 1, 5, 9, 2, 6, 5], "duplicates"),
        ([], "empty"),
        ([42], "single"),
        ([2, 1], "two elements"),
        ([1, 2, 3, 4, 5], "sorted"),
        ([5, 4, 3, 2, 1], "reverse"),
        ([7, 7, 7, 7], "all same"),
        ([-3, 0, 2, -1, 5, -2], "negative"),
        (list(range(100, 0, -1)), "large")
    ]

    for arr, desc in test_cases:
        original = arr.copy()
        expected = sorted(arr)
        heap_sort(arr)
        assert arr == expected, f"{desc}: Expected {expected}, got {arr}"

    print("✓ All sort tests passed")


def main():
    test_heap_operations()
    test_heap_sort()


if __name__ == "__main__":
    main()
