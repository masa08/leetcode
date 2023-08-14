from typing import List


def main():
    args = ["a", "a", "b", "b", "c", "c", "c"]
    solution = Solution()
    result = solution.compress(args)
    print(result)


class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        if length < 2:
            return length

        anchor = 0
        write = 0
        for index, char in enumerate(chars):
            nextIndex = index + 1
            if nextIndex == length or char != chars[nextIndex]:
                chars[write] = char
                write += 1
                if index > anchor:
                    repeated_times = index - anchor + 1
                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1
                anchor = nextIndex

        return write

        # index = 0
        # result = 0

        # while index < len(chars):
        #     group_length = 1
        #     while (index+group_length < len(chars) and chars[index+group_length] == chars[index]):
        #         group_length += 1
        #     chars[result] = chars[index]  # replace the first char in the group
        #     result += 1  # move to the next position

        #     if group_length > 1:
        #         group_length_str = str(group_length)
        #         chars[result:result+len(group_length_str)
        #               ] = list(group_length_str)
        #         result += len(group_length_str)
        #     index += group_length

        # return result


if __name__ == '__main__':
    main()
