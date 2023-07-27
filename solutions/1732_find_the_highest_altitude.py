from typing import List


def main():
    args = [-5, 1, 5, 0, -7]
    solution = Solution()
    result = solution.largestAltitude(args)
    print(result)


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0] * (len(gain)+1)

        for i in range(1, len(altitudes)):
            altitudes[i] = altitudes[i-1] + gain[i-1]

        return max(altitudes)


if __name__ == '__main__':
    main()
