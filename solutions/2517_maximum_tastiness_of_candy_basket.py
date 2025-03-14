from typing import List


def main():
    args = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    result = solution.maximumTastiness(args, 3)
    print(result)


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()  # 絶対値を気にする必要が不要になる
        low, high = 0, price[-1] - price[0]  # differenceを管理
        answer = 0

        def canPick(difference):
            """ differenceの場合、k個の要素をpickできるか """
            count = 1
            prev = price[0]

            for i in range(1, len(price)):
                if price[i] - prev >= difference:
                    count += 1
                    prev = price[i]
                    if count == k:
                        return True
            return False

        while low <= high:
            mid = (low + high) // 2
            if canPick(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer


if __name__ == '__main__':
    main()
