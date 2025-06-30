def main():
    args = [5, 2, 3, 1, 4]
    solution = Solution()
    result = solution.bubble_sort(args)
    print(result)


class Solution:
    def bubble_sort(self, numbers):
        length = len(numbers)
        for i in range(length):
            for j in range(length - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers


if __name__ == '__main__':
    main()
