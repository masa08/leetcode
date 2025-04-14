from collections import deque
from typing import List


def main():
    args = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    result = solution.dailyTemperatures(args)
    print(result)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Using deque for stack
        n = len(temperatures)
        result = [0] * n
        stack = deque([])

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                result[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return result

        # Brute force(time complexity: O(n^2), and time exceeded)
        # n = len(temperatures)
        # result = [0] * n

        # for curr_day, curr_temp in enumerate(temperatures):
        #     day = 0
        #     while curr_day + day < n and curr_temp >= temperatures[curr_day + day]:
        #         day += 1

        #     if curr_day+day < n:
        #         result[curr_day] = day

        # return result

        # Using stack
        # n = len(temperatures)
        # answer = [0] * n
        # stack = []

        # for curr_day, curr_temp in enumerate(temperatures):
        #     while stack and temperatures[stack[-1]] < curr_temp:
        #         prev_day = stack.pop(-1)
        #         answer[prev_day] = curr_day - prev_day
        #     stack.append(curr_day)

        # return answer

        # n = len(temperatures)
        # hottest = 0
        # answer = [0] * n

        # for curr_day in range(n-1, -1, -1):
        #     curr_temp = temperatures[curr_day]

        #     # hottestであれば、answer[curr_day]は0のまま
        #     if curr_temp >= hottest:
        #         hottest = curr_temp
        #         continue

        #     days = 1
        #     # 今日よりも気温が高い日が見つかるまで、answer[curr_day]を加算
        #     while temperatures[curr_day+days] <= curr_temp:
        #         days += answer[curr_day+days]
        #     answer[curr_day] = days

        # return answer


if __name__ == '__main__':
    main()
