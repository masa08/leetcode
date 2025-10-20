# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Binary search approach to find the first bad version.

        Algorithm Overview:
        - Use binary search to efficiently find the first bad version
        - Pattern: Finding boundary between OK and NG (meguru-style binary search)
        - Key insight: If version k is bad, all versions >= k are bad

        Approach:
        1. Initialize ok=0 (always good), ng=n+1 (always bad)
        2. While abs(ok-ng) > 1:
           - Check middle version
           - If good: move ok pointer to mid
           - If bad: move ng pointer to mid
        3. Return ng (first bad version)

        Time Complexity: O(log n)
        - Binary search reduces search space by half each iteration
        - Number of iterations: log₂(n)
        - Each iteration makes 1 API call

        Space Complexity: O(1)
        - Only using constant space for ok, ng, mid pointers
        - No recursion stack (iterative approach)
        """
        ok, ng = 0, n+1

        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if not isBadVersion(mid):
                ok = mid
            else:
                ng = mid

        return ng


def main():
    # Mock isBadVersion API for testing
    global BAD_VERSION

    def mock_isBadVersion(version: int) -> bool:
        return version >= BAD_VERSION

    # Override the global function
    import __main__
    __main__.isBadVersion = mock_isBadVersion

    solution = Solution()

    # Test case 1: n = 5, bad = 4
    BAD_VERSION = 4
    assert solution.firstBadVersion(5) == 4

    # Test case 2: n = 1, bad = 1
    BAD_VERSION = 1
    assert solution.firstBadVersion(1) == 1

    # Edge case: first version is bad
    BAD_VERSION = 1
    assert solution.firstBadVersion(10) == 1

    # Edge case: last version is bad
    BAD_VERSION = 10
    assert solution.firstBadVersion(10) == 10

    # Large scale test
    BAD_VERSION = 1000000
    assert solution.firstBadVersion(2000000) == 1000000

    print("All tests passed!")


if __name__ == "__main__":
    main()
