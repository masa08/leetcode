from typing import Dict


def main():
    args = ["apple", "app"]
    solution = Trie()
    for word in args:
        solution.insert(word)

    print(solution.search("app"))  # Returns True
    print(solution.startsWith("app"))  # Returns True
    print(solution.search("appl"))  # Returns False
    print(solution.startsWith("a"))  # Returns True
    print(solution.startsWith("b"))  # Returns False


class TreeNode:
    def __init__(self):
        self.children: Dict[str, TreeNode] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TreeNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, path: str):
        """Traverse the trie along the path and return the node at the end, or None if not found."""
        current = self.root
        for char in path:
            if char not in current.children:
                return None
            current = current.children[char]
        return current


if __name__ == '__main__':
    main()
