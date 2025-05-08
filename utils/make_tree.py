from model import TreeNode


def makeTree(arr):
    nodes = [TreeNode(value) if value else None for value in arr]
    for i, node in enumerate(nodes):
        if node:
            left = i * 2 + 1
            right = i * 2 + 2
            if left < len(nodes):
                node.left = nodes[left]
            if right < len(nodes):
                node.right = nodes[right]
    return nodes[0]
