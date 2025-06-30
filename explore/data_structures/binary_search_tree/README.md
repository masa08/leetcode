# 二分探索木 (Binary Search Tree)

二分木の性質に加えて、左の子 < 親 < 右の子という順序関係を持つ木構造です。

## 基本概念

### BST の性質
- **左の部分木**: 親ノードより小さい値のみ
- **右の部分木**: 親ノードより大きい値のみ
- **中順走査**: ソート済みの順序で要素を取得

### 基本操作の計算量
- **探索**: 平均 O(log n)、最悪 O(n)
- **挿入**: 平均 O(log n)、最悪 O(n)
- **削除**: 平均 O(log n)、最悪 O(n)

## 基本操作

### 1. 探索 (Search)
```python
def search_bst(root, val):
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)
```

### 2. 挿入 (Insert)
```python
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    
    return root
```

### 3. 削除 (Delete)
```python
def delete_bst(root, key):
    if not root:
        return root
    
    if key < root.val:
        root.left = delete_bst(root.left, key)
    elif key > root.val:
        root.right = delete_bst(root.right, key)
    else:
        # ケース1: 葉ノード
        if not root.left and not root.right:
            return None
        
        # ケース2: 子が1つ
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # ケース3: 子が2つ
        # 右の部分木の最小値で置換
        min_node = find_min(root.right)
        root.val = min_node.val
        root.right = delete_bst(root.right, min_node.val)
    
    return root

def find_min(root):
    while root.left:
        root = root.left
    return root
```

## 重要なパターン

### 1. BST の検証
```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))
```

### 2. 最低共通祖先 (LCA)
```python
def lowest_common_ancestor_bst(root, p, q):
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor_bst(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor_bst(root.right, p, q)
    else:
        return root
```

### 3. k番目に小さい要素
```python
def kth_smallest(root, k):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    return inorder(root)[k-1]

# 効率的な解法
def kth_smallest_optimized(root, k):
    stack = []
    curr = root
    
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right
```

### 4. 範囲内の値の和
```python
def range_sum_bst(root, low, high):
    if not root:
        return 0
    
    if root.val < low:
        return range_sum_bst(root.right, low, high)
    elif root.val > high:
        return range_sum_bst(root.left, low, high)
    else:
        return (root.val + 
                range_sum_bst(root.left, low, high) + 
                range_sum_bst(root.right, low, high))
```

## 構築パターン

### 1. ソート済み配列からBST
```python
def sorted_array_to_bst(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    
    return root
```

### 2. 前順走査からBST復元
```python
def bst_from_preorder(preorder):
    def build(min_val, max_val):
        nonlocal idx
        if idx >= len(preorder):
            return None
        
        val = preorder[idx]
        if val < min_val or val > max_val:
            return None
        
        idx += 1
        root = TreeNode(val)
        root.left = build(min_val, val)
        root.right = build(val, max_val)
        return root
    
    idx = 0
    return build(float('-inf'), float('inf'))
```

## 平衡二分探索木

### AVL木
- **高さバランス**: 左右の部分木の高さの差が1以下
- **回転操作**: 挿入・削除時にバランスを維持

### 赤黒木
- **色の制約**: 各ノードが赤または黒
- **平衡条件**: 赤いノードの子は黒、根から葉への黒ノード数は同じ

## BSTの退化
- **最悪ケース**: 一方向に偏った木（線形リスト状）
- **解決策**: 自己平衡木（AVL、赤黒木）の使用

## 典型的な問題
-  Validate Binary Search Tree
-  Recover Binary Search Tree
-  Convert Sorted Array to Binary Search Tree
-  Convert Sorted List to Binary Search Tree
-  Binary Search Tree Iterator
-  Kth Smallest Element in a BST
-  Lowest Common Ancestor of a BST
-  Delete Node in a BST
-  Minimum Absolute Difference in BST
-  Convert BST to Greater Tree
-  Trim a Binary Search Tree
-  Search in a Binary Search Tree
-  Insert into a Binary Search Tree
-  Range Sum of BST