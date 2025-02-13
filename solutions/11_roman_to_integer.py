from typing import List


def main():
    args = "MCMXCIV"
    solution = Solution()
    result = solution.romanToInt(args)
    print(result)


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M" : 1000}

        prev = 0
        res = 0
        
        for char in s:
            val = mapping[char]
            if prev < val:
                res -= prev
                res += val - prev
            else:
                res += val

            prev = val
        
        return res


if __name__ == '__main__':
    main()
