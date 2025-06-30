"""
Two Pointer Pattern: 逆転に関するパターン集

Two pointerは配列や文字列の操作において、O(n)時間でインプレースに処理を行う
効率的なテクニックです。
"""


def reverse_array(arr: list, left: int, right: int) -> None:
    """
    配列の指定範囲を逆転する基本パターン

    Time: O(n), Space: O(1)

    Args:
        arr: 対象の配列
        left: 開始インデックス
        right: 終了インデックス
    """
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def reverse_string(s: str) -> str:
    """
    文字列を逆転する
    注意: Pythonの文字列はimmutableなので、リストに変換して処理

    Time: O(n), Space: O(n)
    """
    chars = list(s)
    reverse_array(chars, 0, len(chars) - 1)
    return ''.join(chars)


def reverse_words_in_string(s: str) -> str:
    """
    文字列内の単語順を逆転する
    例: "hello world" -> "world hello"

    アプローチ:
    1. 文字列全体を逆転
    2. 各単語を個別に逆転

    Time: O(n), Space: O(n) - Pythonの文字列がimmutableのため
    """
    # 文字のリストに変換
    chars = list(s)
    n = len(chars)

    # Step 1: 全体を逆転
    reverse_array(chars, 0, n - 1)

    # Step 2: 各単語を逆転
    start = 0
    for end in range(n + 1):
        if end == n or chars[end] == ' ':
            reverse_array(chars, start, end - 1)
            start = end + 1

    return ''.join(chars)


def reverse_words_with_cleanup(s: str) -> str:
    """
    余分な空白を除去しながら単語順を逆転する
    LeetCode 151: Reverse Words in a String のパターン

    Time: O(n), Space: O(n)
    """
    # 余分な空白を除去
    words = s.split()

    # Two pointerで単語を逆転
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return ' '.join(words)


def is_palindrome(s: str) -> bool:
    """
    Two pointerを使った回文判定

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# 使用例とテスト
if __name__ == "__main__":
    # 配列の逆転
    arr = [1, 2, 3, 4, 5]
    reverse_array(arr, 0, len(arr) - 1)
    print(f"Reversed array: {arr}")

    # 文字列の逆転
    s = "hello"
    print(f"Reversed string: {reverse_string(s)}")

    # 単語順の逆転
    sentence = "the sky is blue"
    print(f"Reversed words: {reverse_words_in_string(sentence)}")

    # 余分な空白を除去しながら逆転
    messy = "  hello   world  "
    print(f"Cleaned and reversed: '{reverse_words_with_cleanup(messy)}'")

    # 回文判定
    palindrome = "racecar"
    print(f"Is '{palindrome}' palindrome? {is_palindrome(palindrome)}")
