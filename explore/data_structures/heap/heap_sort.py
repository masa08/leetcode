from typing import List


class Solution:
    def heap_sort(self, list: List[int]) -> None:
        def max_heapify(heap_side, index):
            left, right = index * 2 + 1, index * 2 + 2
            largest = index

            if left < heap_side and list[left] > list[largest]:
                largest = left
            if right < heap_side and list[right] > list[largest]:
                largest = right

            if largest != index:
                list[index], list[largest] = list[largest], list[index]
                max_heapify(heap_side, largest)

        # listをmaxHeapに置き換える
        # len(list) // 2 - 1 => internal nodes
        # ref: https://stackoverflow.com/questions/60150272/why-n-2-1-in-heap-sort
        for i in range(len(list) // 2 - 1, -1, -1):
            max_heapify(len(list), i)

        # 最大値を最後尾に入れることを繰り返して、sortを完成させる
        for i in range(len(list) - 1, 0, -1):
            list[i], list[0] = list[0], list[i]
            max_heapify(i, 0)


arr = [7, 3, 2, 5, 6, 10, 9, 8, 1]
Solution().heap_sort(arr)
print(arr)
