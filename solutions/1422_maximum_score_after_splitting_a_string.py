def main():
    solution = Solution()

    # テストケース
    assert solution.maxScore("011101") == 5
    assert solution.maxScore("00111") == 5
    assert solution.maxScore("1111") == 3

    print("All tests passed!")


class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        result = 0

        for i in range(len(s)-1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1

            result = max(result, zeros + ones)

        return result

        # n = len(s)
        # maximum_scores = [0] * n

        # for i in range(1, n):
        #     left = s[:i]
        #     right = s[i:]
        #     left_count = left.count("0")
        #     right_count = right.count("1")
        #     maximum_scores[i] = left_count + right_count

        # return max(maximum_scores)


if __name__ == '__main__':
    main()
