from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.asteroidCollision([5, 10, -5]) == [5, 10]

    # 左向きが勝つケース
    assert solution.asteroidCollision([8, -8]) == []

    # 右向きのみ
    assert solution.asteroidCollision([10, 2, -5]) == [10]

    # 左向きのみ
    assert solution.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]

    print("All tests passed!")


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for asteroid in asteroids:
            while st and st[-1] > 0 and asteroid < 0:
                if st[-1] + asteroid > 0:
                    break
                elif st[-1] + asteroid < 0:
                    st.pop()
                else:
                    st.pop()
                    break
            else:
                st.append(asteroid)

        return st


if __name__ == '__main__':
    main()
