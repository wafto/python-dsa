#!/usr/bin/env python3

from typing import Optional, List

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def insert(node: Optional[TreeNode], val: int) -> TreeNode:
    if not node:
        return TreeNode(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

def min_value_node(node: Optional[TreeNode]) -> Optional[TreeNode]:
    if not node:
        return None
    current = node
    while current and current.left:
        current = current.left
    return current

def remove(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not node:
        return None
    if val < node.val:
        node.left = remove(node.left, val)
        return node
    if val > node.val:
        node.right = remove(node.right, val)
        return node
    if not node.left:
        return node.right
    if not node.right:
        return node.left
    min = min_value_node(node.right)
    node.val = min.val
    node.right = remove(node.right, min.val)
    return node

def inorder(node: Optional[TreeNode]) -> List[int]:
    output = []
    stack = []
    current = node
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        output.append(current.val)
        current = current.right
    return output

def preorder(node: Optional[TreeNode]) -> List[int]:
    output = []
    stack = []
    current = node
    while current or stack:
        while current:
            output.append(current.val)
            stack.append(current)
            current = current.left
        current = stack.pop()
        current = current.right
    return output

""" def postorder(node: Optional[TreeNode]) -> List[int]:
    output = []
    stack = []
    current = node
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        current = current.right
    return output """


if __name__=="__main__":
    data = [4, 3, 6, 2, 5, 7, 8]

    tree = None

    for num in data:
        tree = insert(tree, num)

    print(tree.val, tree.left.val, tree.right.val)
    print(min_value_node(tree).val, min_value_node(tree.right).val)

    tree = remove(tree, 8)
    print(tree.val, tree.left.val, tree.right.val)

    sorted = inorder(tree)
    print(sorted)

    presorted = preorder(tree)
    print(presorted)

    #postsorted = postorder(tree)
    #print(postsorted)
