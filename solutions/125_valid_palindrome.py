def main():
    args = "A man, a plan, a canal: Panama"
    solution = Solution()
    result = solution.isPalindrome(args)
    print(result)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # parse s and arrange it
        s = s.lower()
        aplhanumeric = [chr(i) for i in range(97, 97+26)] + \
            [str(i) for i in range(0, 10)]
        arranged = ""
        for i in range(len(s)):
            if s[i] in aplhanumeric:
                arranged += s[i]

        # check if palindrome
        left, right = 0, len(arranged)-1
        while left < right:
            if arranged[left] == arranged[right]:
                left += 1
                right -= 1
            else:
                return False

        return True


if __name__ == '__main__':
    main()
