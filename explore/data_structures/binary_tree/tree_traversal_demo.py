"""
Binary Tree Traversal Visualization
3つの走査方法（preorder, inorder, postorder）の動きを具体的に理解する
"""

from typing import List, Optional
import sys
sys.path.append('/Users/masatakaushijima/Development/leetcode')
from model.tree_node import TreeNode


def build_sample_tree() -> TreeNode:
    """
    サンプルツリーを構築:
           1
          / \
         2   3
        / \
       4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def preorder_with_trace(root: Optional[TreeNode]) -> List[int]:
    """
    Preorder (前順): Root → Left → Right

    処理順序:
    1. まず現在のノードを処理
    2. 次に左の子を処理
    3. 最後に右の子を処理
    """
    result = []
    depth = [0]  # 深さをトラッキング

    def traverse(node: Optional[TreeNode], indent: int):
        if not node:
            print(f"{'  ' * indent}└─ None (return)")
            return

        # ① 現在のノードを処理（訪問）
        print(f"{'  ' * indent}└─ 訪問: {node.val} ★")
        result.append(node.val)

        # ② 左の子を処理
        print(f"{'  ' * indent}  ├─ 左へ")
        traverse(node.left, indent + 1)

        # ③ 右の子を処理
        print(f"{'  ' * indent}  └─ 右へ")
        traverse(node.right, indent + 1)

    print("\n=== Preorder Traversal (Root → Left → Right) ===")
    traverse(root, 0)
    return result


def inorder_with_trace(root: Optional[TreeNode]) -> List[int]:
    """
    Inorder (中順): Left → Root → Right

    処理順序:
    1. まず左の子を処理
    2. 次に現在のノードを処理
    3. 最後に右の子を処理
    """
    result = []

    def traverse(node: Optional[TreeNode], indent: int):
        if not node:
            print(f"{'  ' * indent}└─ None (return)")
            return

        print(f"{'  ' * indent}└─ 到達: {node.val}")

        # ① 左の子を処理
        print(f"{'  ' * indent}  ├─ 左へ")
        traverse(node.left, indent + 1)

        # ② 現在のノードを処理（訪問）
        print(f"{'  ' * indent}  ├─ 訪問: {node.val} ★")
        result.append(node.val)

        # ③ 右の子を処理
        print(f"{'  ' * indent}  └─ 右へ")
        traverse(node.right, indent + 1)

    print("\n=== Inorder Traversal (Left → Root → Right) ===")
    traverse(root, 0)
    return result


def postorder_with_trace(root: Optional[TreeNode]) -> List[int]:
    """
    Postorder (後順): Left → Right → Root

    処理順序:
    1. まず左の子を処理
    2. 次に右の子を処理
    3. 最後に現在のノードを処理
    """
    result = []

    def traverse(node: Optional[TreeNode], indent: int):
        if not node:
            print(f"{'  ' * indent}└─ None (return)")
            return

        print(f"{'  ' * indent}└─ 到達: {node.val}")

        # ① 左の子を処理
        print(f"{'  ' * indent}  ├─ 左へ")
        traverse(node.left, indent + 1)

        # ② 右の子を処理
        print(f"{'  ' * indent}  ├─ 右へ")
        traverse(node.right, indent + 1)

        # ③ 現在のノードを処理（訪問）
        print(f"{'  ' * indent}  └─ 訪問: {node.val} ★")
        result.append(node.val)

    print("\n=== Postorder Traversal (Left → Right → Root) ===")
    traverse(root, 0)
    return result


def main():
    """3つの走査方法を実行して結果を比較"""

    print("""
サンプルツリー構造:
       1
      / \\
     2   3
    / \\
   4   5
    """)

    root = build_sample_tree()

    # 3つの走査方法を実行
    preorder_result = preorder_with_trace(root)
    inorder_result = inorder_with_trace(root)
    postorder_result = postorder_with_trace(root)

    # 結果のまとめ
    print("\n" + "="*60)
    print("結果まとめ:")
    print("="*60)
    print(f"Preorder  (Root→Left→Right): {preorder_result}")
    print(f"Inorder   (Left→Root→Right): {inorder_result}")
    print(f"Postorder (Left→Right→Root): {postorder_result}")

    print("\n" + "="*60)
    print("覚え方:")
    print("="*60)
    print("Preorder:  親を「先に」訪問してから子へ")
    print("Inorder:   左の子 → 親 → 右の子（「中間」で親）")
    print("Postorder: 子を全部訪問してから「最後に」親")
    print("="*60)


if __name__ == "__main__":
    main()
