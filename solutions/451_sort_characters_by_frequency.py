import collections


def main():
    solution = Solution()

    # 基本ケース
    assert solution.frequencySort("tree") in ["eert", "eetr"]
    assert solution.frequencySort("cccaaa") in ["cccaaa", "aaaccc"]
    assert solution.frequencySort("Aabb") in ["bbAa", "bbaA"]

    # エッジケース
    assert solution.frequencySort("") == ""
    assert solution.frequencySort("a") == "a"

    print("All tests passed!")


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s

        counts = collections.Counter(s)
        max_freq = max(counts.values())

        buckets = [[] for _ in range(max_freq + 1)]
        for char, cnt in counts.items():
            buckets[cnt].append(char)

        sb = []
        for cnt in range(len(buckets)-1, 0, -1):
            bucket = buckets[cnt]
            for c in bucket:
                sb.append(c * cnt)

        return "".join(sb)


if __name__ == '__main__':
    main()
