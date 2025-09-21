import heapq
from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.kthLargestNumber(["3", "6", "7", "10"], 4) == "3"
    assert solution.kthLargestNumber(["2", "21", "12", "1"], 3) == "2"

    # エッジケース
    assert solution.kthLargestNumber(["0"], 1) == "0"
    assert solution.kthLargestNumber(["1000000000"], 1) == "1000000000"

    # 大きな数値
    assert solution.kthLargestNumber(
        ["683339452288515879", "7846081062003424420", "4805719838"], 2) == "683339452288515879"

    print("All tests passed!")


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) * -1 for num in nums]
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)

        result = heapq.heappop(nums) * -1

        return str(result)


if __name__ == '__main__':
    main()
