from typing import List


def main():
    args = ["a", "a", "b", "b", "c", "c", "c"]
    solution = Solution()
    result = solution.compress(args)
    print(result)


class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        result = 0

        while index < len(chars):
            group_length = 1
            while (index+group_length < len(chars) and chars[index+group_length] == chars[index]):
                group_length += 1
            chars[result] = chars[index]  # replace the first char in the group
            result += 1  # move to the next position

            if group_length > 1:
                group_length_str = str(group_length)
                chars[result:result+len(group_length_str)
                      ] = list(group_length_str)
                result += len(group_length_str)
            index += group_length

        return result


if __name__ == '__main__':
    main()
