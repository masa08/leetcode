from typing import List


def main():
    codec = Codec()

    # Basic case
    strs1 = ["Hello", "World"]
    assert codec.decode(codec.encode(strs1)) == strs1

    # Edge cases
    strs2 = []
    assert codec.decode(codec.encode(strs2)) == strs2

    strs3 = [""]
    assert codec.decode(codec.encode(strs3)) == strs3

    strs4 = ["", "abc", ""]
    assert codec.decode(codec.encode(strs4)) == strs4

    # Strings containing the delimiter
    strs5 = ["a#b", "c#d"]
    assert codec.decode(codec.encode(strs5)) == strs5

    print("All tests passed!")


class Codec:
    """
    Length-prefix encoding: write each string as `length#content`.
    Decoding reads the length first, so the content can contain any
    characters (including '#') without ambiguity.

    Example:
      encode(["abc", "de"]) → "3#abc2#de"
      decode("3#abc2#de")   → ["abc", "de"]

    Time: O(n) for both encode and decode (n = total characters)
    Space: O(n)
    """

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            delim = s.index('#', i)
            length = int(s[i:delim])
            start = delim + 1
            end = start + length
            result.append(s[start:end])
            i = end

        return result


if __name__ == '__main__':
    main()
