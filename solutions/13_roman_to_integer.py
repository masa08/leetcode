from typing import List


def main():
    args = "MCMXCIV"
    solution = Solution()
    result = solution.romanToInt(args)
    print(result)


mapping = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and mapping[s[i]] < mapping[s[i+1]]:
                total += mapping[s[i+1]] - mapping[s[i]]
                i += 2
            else:
                total += mapping[s[i]]
                i += 1

        return total

        # My solution
        # prev = 0
        # res = 0

        # for char in s:
        #     val = mapping[char]
        #     if prev < val:
        #         res -= prev
        #         res += val - prev
        #     else:
        #         res += val

        #     prev = val

        # return res


if __name__ == '__main__':
    main()
