from typing import List


def main():
    solution = Solution()

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]

    # Basic cases
    assert solution.exist([row[:] for row in board], "ABCCED") is True
    assert solution.exist([row[:] for row in board], "SEE") is True
    assert solution.exist([row[:] for row in board],
                          "ABCB") is False  # Can't reuse B

    # Edge cases
    assert solution.exist([["A"]], "A") is True
    assert solution.exist([["A"]], "B") is False

    print("All tests passed!")


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Backtracking + DFS.
        For each cell, try to match the word starting from there.
        Mark visited cells temporarily, restore them after backtracking.

        Time: O(m*n * 4^L) - L = len(word). Each cell starts a DFS,
              each step has up to 4 directions and depth L.
        Space: O(L) - recursion depth
        """
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, k):
            if k == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            if board[r][c] != word[k]:
                return False

            # Mark as visited by overwriting with '#' (won't match any word char).
            # Alternative: use a `visited` set — costs O(L) extra space but keeps
            # board immutable. We use '#' here for O(1) extra space.
            temp = board[r][c]
            board[r][c] = '#'

            found = any(dfs(r + dr, c + dc, k + 1) for dr, dc in directions)

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False


if __name__ == '__main__':
    main()
