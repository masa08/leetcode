def main():
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = end = 0

        while start < len(nums) and end < len(nums):
            # 数字が連続している場合
            if end + 1 < len(nums) and nums[end] + 1 == nums[end+1]:
                end = end + 1
            else:
                if start == end:
                    result.append(str(nums[start]))
                    start = start + 1
                    end = end + 1
                else:
                    result.append(str(nums[start])+'->'+str(nums[end]))
                    start = end + 1
                    end = end + 1

        return result


if __name__ == '__main__':
    main()
