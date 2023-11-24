def main():
    args = "xyzzaz"
    solution = Solution()
    result = solution.countGoodSubstrings(args)
    print(result)


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left, right = 0, 2
        l = len(s)
        res = 0

        while right < l:
            substring = s[left:right+1]
            count = len(set(list(substring)))
            if count == 3:
                res += 1
            left += 1
            right += 1

        return res


if __name__ == '__main__':
    main()
