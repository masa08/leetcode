def main():
    args = [5, 2, 3, 1, 4]
    solution = Solution()
    result = solution.merge_sort(args)
    print(result)


class Solution:
    def merge_sort(self, numbers):
        if len(numbers) <= 1:
            return numbers

        center = len(numbers) // 2
        left = numbers[:center]
        right = numbers[center:]

        self.merge_sort(left)
        self.merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        # 考慮されなかった余った部分に対する処理
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

        return numbers


if __name__ == '__main__':
    main()
