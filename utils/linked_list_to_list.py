from typing import Optional
from model import ListNode


def linkedListToList(node: Optional[ListNode]) -> list:
    """LinkedListを配列に変換する

    Args:
        node: LinkedListの先頭ノード

    Returns:
        LinkedListの値を格納した配列
    """
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result
