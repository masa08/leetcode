# 二分木 (Binary Tree)

各ノードが最大2つの子を持つ木構造とその操作パターンです。

## 基本概念

### 二分木の性質
- **左の子**: 各ノードの左側の子ノード
- **右の子**: 各ノードの右側の子ノード
- **葉ノード**: 子を持たないノード
- **高さ**: ルートから最深の葉までの距離

### ノードの構造
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## 重要な走査方法

### 1. 深さ優先探索 (DFS)
```python
# 前順走査 (Pre-order): Root → Left → Right
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# 中順走査 (In-order): Left → Root → Right  
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# 後順走査 (Post-order): Left → Right → Root
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### 2. 幅優先探索 (BFS) - レベル順走査
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

## 重要なパターン

### 1. 木の高さ・深さ
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def min_depth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    
    left = min_depth(root.left) if root.left else float('inf')
    right = min_depth(root.right) if root.right else float('inf')
    return 1 + min(left, right)
```

### 2. バランス判定
```python
def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return check_height(root) != -1
```

### 3. 経路の和
```python
def has_path_sum(root, target_sum):
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == target_sum
    
    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))
```

### 4. 最低共通祖先 (LCA)
```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left or right
```

### 5. 対称性判定
```python
def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    return is_mirror(root.left, root.right)
```

## 構築パターン

### 1. 配列から木を構築
```python
def array_to_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        node = queue.popleft()
        
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root
```

### 2. 前順・中順から木を構築
```python
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    root_index = inorder.index(root_val)
    
    root.left = build_tree(preorder[1:1+root_index], 
                          inorder[:root_index])
    root.right = build_tree(preorder[1+root_index:], 
                           inorder[root_index+1:])
    
    return root
```

## 特殊な木の種類
- **完全二分木**: 最下段以外は全て埋まっている
- **満二分木**: 全ての内部ノードが2つの子を持つ
- **平衡二分木**: 左右の部分木の高さの差が1以下

## 典型的な問題
-  Binary Tree Inorder Traversal
-  Same Tree
-  Symmetric Tree
-  Binary Tree Level Order Traversal
-  Maximum Depth of Binary Tree
-  Balanced Binary Tree
-  Minimum Depth of Binary Tree
-  Path Sum
-  Path Sum II
-  Binary Tree Maximum Path Sum
-  Binary Tree Right Side View
-  Invert Binary Tree
-  Lowest Common Ancestor of a BST
-  Lowest Common Ancestor of a Binary Tree
-  Path Sum III