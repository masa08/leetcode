def main():
    args = [4, 5, 6, 7, 0, 1, 2]
    solution = Solution()
    result = solution.search(args, 0)
    print(result)


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            # 昇順である
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # rotateにより、昇順ではない
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


if __name__ == '__main__':
    main()
