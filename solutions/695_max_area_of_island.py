
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Algorithm: DFS (Depth-First Search) to explore each island and find max area

        1. Scan entire grid
        2. When land (1) is found, perform DFS to explore entire island
        3. Mark visited cells as 0 (prevent revisiting)
        4. Calculate area of each island and update maximum

        Complexity:
        Time:  O(M × N) - Each cell visited at most once
        Space: O(M × N) - Recursion stack depth (worst case: entire grid is one island)
        """
        M, N, maxArea = len(grid), len(grid[0]), 0

        def dfs_area(x, y):
            """
            Calculate island area using DFS

            Time:  O(island size) - Visit each cell in island once
            Space: O(island size) - Recursion stack depth
            """
            # Boundary check & water/visited check
            if not (0 <= x < M and 0 <= y < N and grid[x][y] == 1):
                return 0

            # Mark as visited (prevent revisiting)
            grid[x][y] = 0

            # Count current cell in area
            area = 1

            # Explore 4 directions (up, right, down, left) and add to area
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                area += dfs_area(x + dx, y + dy)

            return area

        # Scan entire grid: O(M × N)
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    # Found new island, calculate its area with DFS
                    maxArea = max(maxArea, dfs_area(i, j))

        return maxArea


def main():
    solution = Solution()

    # Test case 1: Basic island
    grid1 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    assert solution.maxAreaOfIsland(grid1) == 6
    print("Test 1 passed: max area = 6 ✓")

    # Test case 2: All water
    grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert solution.maxAreaOfIsland(grid2) == 0
    print("Test 2 passed: max area = 0 ✓")

    # Test case 3: Single island
    grid3 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    assert solution.maxAreaOfIsland(grid3) == 4
    print("Test 3 passed: max area = 4 ✓")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    main()
