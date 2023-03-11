from typing import List


def main():
    args = [1, 0, 2, 3, 0, 4, 5, 0]
    solution = Solution()
    result = solution.duplicateZeros(args)
    print(result)


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        curr = 0

        while curr < length:
            if arr[curr] == 0:
                current = arr[:curr]
                current.append(0)
                left = arr[curr:length-1]
                arr[:] = current + left
                curr += 2
            else:
                curr += 1

        print(arr)


if __name__ == '__main__':
    main()
