from typing import List


def main():
    args = [5, 10, -5]
    solution = Solution()
    result = solution.asteroidCollision(args)
    print(result)


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # initialize stack
        st = []

        # itelate asteroids
        for asteroid in asteroids:
            while st and st[-1] > 0 and asteroid < 0:
                if st[-1] + asteroid < 0:
                    st.pop()
                elif st[-1] + asteroid > 0:
                    break
                else:
                    st.pop()
                    break
            else:
                st.append(asteroid)

        return st


if __name__ == '__main__':
    main()
