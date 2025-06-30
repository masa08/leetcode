# トライ木 (Trie)

文字列の集合を効率的に格納・検索するためのツリー構造です。

## 基本概念

### トライ木の特徴
- **接頭辞木**: 共通の接頭辞を共有
- **効率的な検索**: O(m) - mは文字列の長さ
- **スペース効率**: 共通接頭辞の共有でメモリ節約

### ノードの構造
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # 文字 -> TrieNode
        self.is_end = False  # 単語の終端フラグ
```

### 基本操作
```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

## 重要なパターン

### 1. 単語検索 (Word Search)
```python
def find_words(board, words):
    # Trieに全単語を挿入
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    def dfs(i, j, node, path):
        # DFS + Trie pruning
        if node.is_end:
            result.add(path)
        
        # 4方向探索
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i + di, j + dj
            if (0 <= ni < m and 0 <= nj < n and 
                board[ni][nj] in node.children):
                # バックトラッキング
                char = board[ni][nj]
                board[ni][nj] = '#'  # 訪問マーク
                dfs(ni, nj, node.children[char], path + char)
                board[ni][nj] = char  # 復元
```

### 2. 最大XOR
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # 0 or 1
        
def find_max_xor(nums):
    trie = TrieNode()
    
    # 全数値をバイナリでTrieに挿入
    for num in nums:
        node = trie
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    max_xor = 0
    for num in nums:
        node = trie
        current_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # 反対のビットを探す（XOR最大化）
            toggled = 1 - bit
            if toggled in node.children:
                current_xor |= (1 << i)
                node = node.children[toggled]
            else:
                node = node.children[bit]
        max_xor = max(max_xor, current_xor)
    
    return max_xor
```

### 3. 自動補完
```python
def autocomplete(trie, prefix):
    node = trie.root
    # プレフィックスまで移動
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]
    
    # DFSで全ての候補を収集
    suggestions = []
    def dfs(node, current_word):
        if node.is_end:
            suggestions.append(prefix + current_word)
        for char, child in node.children.items():
            dfs(child, current_word + char)
    
    dfs(node, "")
    return suggestions
```

### 4. 単語分割
```python
def word_break(s, word_dict):
    trie = Trie()
    for word in word_dict:
        trie.insert(word)
    
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        node = trie.root
        for j in range(i - 1, -1, -1):
            char = s[j]
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end and dp[j]:
                dp[i] = True
                break
    
    return dp[n]
```

## 最適化テクニック

### 1. 配列による子ノード管理
```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # a-z
        self.is_end = False
    
    def get_index(self, char):
        return ord(char) - ord('a')
```

### 2. 圧縮Trie (Radix Tree)
- 一本道の連続するノードを圧縮
- スペース効率の改善

### 3. 遅延削除
- 削除時にノードを即座に削除せず、フラグで管理

## 計算量
- **挿入**: O(m) - mは文字列長
- **検索**: O(m)
- **プレフィックス検索**: O(p) - pはプレフィックス長
- **スペース**: O(ALPHABET_SIZE × N × M) 最悪ケース

## vs その他のデータ構造

### vs ハッシュテーブル
- **Trie**: プレフィックス検索、ソート順、メモリ効率
- **Hash**: 完全一致検索の高速性

### vs 配列
- **Trie**: 動的な単語追加、プレフィックス操作
- **Array**: シンプルさ、メモリ効率（静的）

## 典型的な問題
-  Implement Trie (Prefix Tree)
-  Design Add and Search Words Data Structure
-  Word Search II
-  Palindrome Pairs
-  Maximum XOR of Two Numbers in an Array
-  Word Squares
-  Concatenated Words
-  Design In-Memory File System
-  Replace Words
-  Implement Magic Dictionary
-  Map Sum Pairs
-  Longest Word in Dictionary