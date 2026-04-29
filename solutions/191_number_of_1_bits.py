def main():
    solution = Solution()

    # Basic cases
    assert solution.hammingWeight(11) == 3       # 1011
    assert solution.hammingWeight(128) == 1      # 10000000
    assert solution.hammingWeight(2147483645) == 30

    # Edge cases
    assert solution.hammingWeight(0) == 0        # No bits set
    assert solution.hammingWeight(1) == 1        # Single bit

    print("All tests passed!")


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Brian Kernighan's algorithm: n & (n - 1) clears the lowest set bit.
        Loop until n becomes 0; the number of iterations equals the number of 1 bits.

        Why this works:
          n     = 1011
          n - 1 = 1010   (subtracting 1 flips the lowest 1 and all bits after it)
          n & (n-1) = 1010  → the lowest 1 bit is cleared

        Time: O(k) where k = number of set bits (faster than O(32))
        Space: O(1)
        """
        count = 0
        while n:
            # Formula: `n & (n - 1)` clears the lowest set bit of n.
            # Repeat until n becomes 0; the loop count equals the number of 1 bits.
            n = n & (n - 1)
            count += 1
        return count

    def hammingWeight_naive(self, n: int) -> int:
        """
        Naive: check each bit one by one by shifting right.

        Time: O(32) - always 32 iterations for 32-bit int
        Space: O(1)
        """
        count = 0
        while n:
            count += n & 1   # Check lowest bit
            n >>= 1          # Shift right by 1
        return count


if __name__ == '__main__':
    main()
