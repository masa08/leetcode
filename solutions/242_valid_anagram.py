from collections import defaultdict


def main():
    solution = Solution()

    # Test cases
    assert solution.isAnagram("anagram", "nagaram") == True
    assert solution.isAnagram("rat", "car") == False
    assert solution.isAnagram("", "") == True
    assert solution.isAnagram("a", "a") == True
    assert solution.isAnagram("ab", "ba") == True

    print("All tests passed!")


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        for i in range(len(s)):
            s_hash[s[i]] += 1
            t_hash[t[i]] += 1

        for k, v in s_hash.items():
            if k in t_hash:
                if t_hash[k] == v:
                    continue
            return False

        return True

        # if len(s) != len(t):
        #     return False

        # counter = [0] * 26  # アルファベットの数だけ

        # for i in range(len(s)):
        #     counter[ord(s[i]) - ord('a')] += 1
        #     counter[ord(t[i]) - ord('a')] -= 1

        # for count in counter:
        #     if count != 0:
        #         return False

        # return True


if __name__ == '__main__':
    main()
