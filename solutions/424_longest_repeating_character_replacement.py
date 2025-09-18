from collections import defaultdict


def main():
    solution = Solution()

    # テストケース1: 基本的なケース
    s1 = "ABAB"
    k1 = 2
    assert solution.characterReplacement(s1, k1) == 4

    # テストケース2: 全て同じ文字にできる
    s2 = "AABABBA"
    k2 = 1
    assert solution.characterReplacement(s2, k2) == 4

    # テストケース3: 単一文字
    s3 = "A"
    k3 = 0
    assert solution.characterReplacement(s3, k3) == 1

    # テストケース4: 全て異なる文字
    s4 = "ABCDE"
    k4 = 1
    assert solution.characterReplacement(s4, k4) == 2

    print("All tests passed!")


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        max_length = 0
        count = defaultdict(int)

        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == '__main__':
    main()
