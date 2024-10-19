from typing import List


def main():
    args = [1, 1, 1, 2, 2, 3]
    solution = Solution()
    result = solution.topKFrequent(args, 2)
    print(result)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1

        sorted_items = sorted(mapping.items(), key=lambda item: item[1])

        result = []
        for _ in range(k):
            k, _ = sorted_items.pop()
            result.append(k)

        return result


if __name__ == '__main__':
    main()
