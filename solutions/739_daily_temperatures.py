from typing import List


def main():
    args = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    result = solution.dailyTemperatures(args)
    print(result)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop(-1)
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)

        return answer


if __name__ == '__main__':
    main()
