from typing import List
from collections import Counter


def main():
    solution = Solution()

    # 基本ケース
    assert solution.commonChars(["bella", "label", "roller"]) == [
        "e", "l", "l"]
    assert solution.commonChars(["cool", "lock", "cook"]) == ["c", "o"]

    # エッジケース
    assert solution.commonChars(["a"]) == ["a"]
    assert solution.commonChars(["abc", "abc", "abc"]) == ["a", "b", "c"]

    # v2のテスト
    assert solution.commonChars_v2(["bella", "label", "roller"]) == [
        "e", "l", "l"]
    assert solution.commonChars_v2(["cool", "lock", "cook"]) == ["c", "o"]
    assert solution.commonChars_v2(["a"]) == ["a"]
    assert solution.commonChars_v2(["abc", "abc", "abc"]) == ["a", "b", "c"]

    print("All tests passed!")


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        num_of_letters = 26
        min_freq = [0] * num_of_letters

        for c in words[0]:
            min_freq[ord(c) - ord('a')] += 1

        for word in words[1:]:
            freq = [0] * num_of_letters
            for c in word:
                freq[ord(c) - ord('a')] += 1

            for i in range(num_of_letters):
                min_freq[i] = min(min_freq[i], freq[i])

        res = []
        for i in range(num_of_letters):
            for _ in range(min_freq[i]):
                res.append(chr(i + ord('a')))

        return res

    def commonChars_v2(self, words: List[str]) -> List[str]:
        """
        別解: collections.Counterを使用したシンプルな実装
        """
        # 最初の単語の文字頻度から開始
        common = Counter(words[0])

        # 各単語と交差を取る（&演算子で最小値を自動的に取得）
        for word in words[1:]:
            common &= Counter(word)

        # Counterをリストに展開（各文字をカウント分だけ追加）
        return list(common.elements())


if __name__ == '__main__':
    main()
