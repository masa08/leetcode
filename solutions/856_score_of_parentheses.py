def main():
    solution = Solution()

    # 基本ケース
    assert solution.scoreOfParentheses("()") == 1
    assert solution.scoreOfParentheses("(())") == 2
    assert solution.scoreOfParentheses("()()") == 2

    # 複雑なケース
    assert solution.scoreOfParentheses("(()(()))") == 6
    assert solution.scoreOfParentheses("(()())") == 4

    print("All tests passed!")


class Solution:
    """
    スコア計算ルール：
    1. "()" = 1点（基本ペア）
    2. AB = A + B（隣接する括弧グループは足し算）
    3. (A) = 2 * A（括弧で囲まれた内側のスコアは2倍）

    例：
    "()" → 1
    "()()" → 1 + 1 = 2
    "(())" → 2 × 1 = 2
    "(()(()))" → 2 × (1 + 2) = 6

    アルゴリズム：
    - スタックを使用して計算をシミュレート
    - '('を見たら'x'をプッシュ（開き括弧のマーカー）
    - ')'を見たら：
      - [..., x, x]の場合 → [..., 1]（基本ペア）
      - [..., x, num]の場合 → [..., 2 * num]（囲まれた値を2倍）
      - [..., num, num]の場合 → [..., num + num]（隣接する値を足す）
    """

    def scoreOfParentheses(self, s: str) -> int:
        # 各階層のスコアを管理するスタック
        # 新しい'('で新階層開始（0で初期化）
        score_stack = [0]
        
        for char in s:
            if char == '(':
                # 新しい階層を開始
                score_stack.append(0)
            else:  # char == ')'
                # 現在の階層のスコアを取得
                current_score = score_stack.pop()
                
                # スコア計算：
                # - current_score == 0 なら "()" パターン → 1点
                # - current_score > 0 なら "(A)" パターン → 2倍
                if current_score == 0:
                    score_to_add = 1
                else:
                    score_to_add = 2 * current_score
                
                # 親階層にスコアを追加
                score_stack[-1] += score_to_add
        
        return score_stack[0]


if __name__ == '__main__':
    main()
