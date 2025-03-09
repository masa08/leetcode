def main():
    args = [2, 6, 5]
    solution = Solution()
    result = solution.minFlips(*args)
    print(result)


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0

        while a > 0 or b > 0 or c > 0:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if (a_bit | b_bit) != c_bit:
                if c_bit == 1:
                    count += 1  # 1,0 or 0,1にするため、a, b のどちらかを1にする
                else:
                    count += a_bit + b_bit  # 0,0にするため、a,bが1の場合は反転
            a >>= 1
            b >>= 1
            c >>= 1

        return count


if __name__ == '__main__':
    main()
