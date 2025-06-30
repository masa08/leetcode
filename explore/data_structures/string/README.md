# 文字列 (String)

文字の配列として実装される、テキストデータを扱うデータ構造です。

## 基本概念

### 文字列の特徴
- **文字の集合**: 連続した文字を格納
- **Immutable（Python）**: 一度作成すると変更不可
- **Unicode対応**: 多言語文字に対応

### Python での文字列
```python
# 文字列リテラル
s = "Hello, World!"
s = 'Single quotes'
s = """Multi-line
string"""

# 文字列は immutable
s[0] = 'h'  # TypeError: 'str' object does not support item assignment
```

## 基本操作

### 1. アクセス・スライス - O(1) / O(k)
```python
s = "Python"
print(s[0])      # 'P' - O(1)
print(s[-1])     # 'n' - O(1)
print(s[1:4])    # 'yth' - O(k)
print(s[::-1])   # 'nohtyP' - O(n)
```

### 2. 連結 - O(n)
```python
# 非効率（新しい文字列を作成）
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2  # O(n)

# 効率的（多数の文字列結合）
parts = ["Hello", " ", "World"]
result = "".join(parts)  # O(n)
```

### 3. 検索 - O(n)
```python
s = "Hello World"
pos = s.find("World")     # 6 (見つからない場合は -1)
pos = s.index("World")    # 6 (見つからない場合は ValueError)
exists = "World" in s     # True
```

### 4. 分割・結合
```python
# 分割
s = "apple,banana,cherry"
fruits = s.split(",")     # ['apple', 'banana', 'cherry']

# 結合
result = "-".join(fruits) # "apple-banana-cherry"
```

## 文字列の内部表現

### エンコーディング
- **ASCII**: 7ビット、英数字・記号
- **UTF-8**: 可変長、Unicode対応
- **UTF-16**: 2バイト単位、Javaの内部表現

### メモリ効率
```python
# 文字列プール（インターン）
a = "hello"
b = "hello"
print(a is b)  # True (同じオブジェクト)

# 長い文字列は別オブジェクト
c = "hello" * 1000
d = "hello" * 1000
print(c is d)  # False
```

## 文字列アルゴリズム

### 1. 文字列マッチング
```python
# KMP法（Knuth-Morris-Pratt）
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    lps = build_lps(pattern)
    i = j = 0
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            return i - j  # マッチ位置
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1
```

### 2. ローリングハッシュ
```python
def rolling_hash(s, pattern_len):
    """文字列の部分文字列のハッシュを効率的に計算"""
    base = 31
    mod = 10**9 + 7
    
    hash_val = 0
    power = 1
    
    # 最初のウィンドウのハッシュ
    for i in range(pattern_len):
        hash_val = (hash_val + ord(s[i]) * power) % mod
        if i < pattern_len - 1:
            power = (power * base) % mod
    
    yield hash_val
    
    # ローリングハッシュ
    for i in range(pattern_len, len(s)):
        # 古い文字を削除、新しい文字を追加
        hash_val = (hash_val - ord(s[i - pattern_len])) % mod
        hash_val = (hash_val * base + ord(s[i])) % mod
        yield hash_val
```

## 文字列変換

### 1. 大文字・小文字変換
```python
s = "Hello World"
print(s.lower())     # "hello world"
print(s.upper())     # "HELLO WORLD"
print(s.title())     # "Hello World"
print(s.swapcase())  # "hELLO wORLD"
```

### 2. 文字の判定
```python
c = 'A'
print(c.isalpha())   # True (アルファベット)
print(c.isdigit())   # False (数字)
print(c.isalnum())   # True (英数字)
print(c.islower())   # False (小文字)
print(c.isupper())   # True (大文字)
```

### 3. 文字列の正規化
```python
import unicodedata

# Unicode正規化
s = "café"  # é は複合文字の場合がある
normalized = unicodedata.normalize('NFC', s)
```

## パフォーマンスの考慮

### 1. 文字列結合
```python
# 悪い例：O(n²)
result = ""
for i in range(n):
    result += str(i)

# 良い例：O(n)
parts = []
for i in range(n):
    parts.append(str(i))
result = "".join(parts)
```

### 2. 文字列比較
```python
# 辞書順比較：O(min(len(s1), len(s2)))
s1 = "apple"
s2 = "application"
print(s1 < s2)  # True
```

## 典型的な問題
- Valid Palindrome
- Longest Substring Without Repeating Characters
- String to Integer (atoi)
- Implement strStr()
- Longest Common Prefix
- Valid Anagram
- Group Anagrams
- Reverse String
- Reverse Words in a String
- String Compression