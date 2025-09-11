def main():
    solution = Solution()

    # 基本ケース
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
    assert solution.isPalindrome("race a car") == False

    # エッジケース
    assert solution.isPalindrome("") == True  # 空文字列
    assert solution.isPalindrome("a") == True  # 単一文字
    assert solution.isPalindrome(" ") == True  # スペースのみ

    # 特殊ケース
    assert solution.isPalindrome(".,") == True  # 記号のみ
    assert solution.isPalindrome("0P") == False  # 数字と文字

    print("All tests passed!")


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1: Two Pointers (最適解)
        # 時間計算量: O(n) - 各文字を最大1回訪問
        # 空間計算量: O(1) - 追加のメモリ使用なし
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

        # Solution 2: リスト内包表記とスライス
        # 時間計算量: O(n) - フィルタリングO(n) + 反転O(n) + 比較O(n)
        # 空間計算量: O(n) - フィルタ後の文字列と反転文字列を保存
        # s = s.lower()
        # arranged = [c for c in s if c.isalnum()]
        # return arranged == arranged[::-1]

        # Solution 3: 手動フィルタリングとTwo Pointers
        # 時間計算量: O(n) - フィルタリングO(n) + 回文チェックO(n)
        # 空間計算量: O(n) - フィルタ後の文字列を保存
        # s = s.lower()
        # aplhanumeric = [chr(i) for i in range(97, 97+26)] + \
        #     [str(i) for i in range(0, 10)]
        # arranged = ""
        # for i in range(len(s)):
        #     if s[i] in aplhanumeric:
        #         arranged += s[i]

        # left, right = 0, len(arranged)-1
        # while left < right:
        #     if arranged[left] == arranged[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         return False

        # return True


if __name__ == '__main__':
    main()
