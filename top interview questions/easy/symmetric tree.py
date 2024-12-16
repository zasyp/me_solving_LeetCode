# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode):
    if root is None:
        return True

    stack = [(root.left, root.right)]

    while stack:
        left, right = stack.pop()
        if not left and not right:
            continue

        # Если только один из них отсутствует или значения не совпадают
        if not left or not right or left.value != right.value:
            return False

        stack.append((left.left, right.right))  # Внешние узлы
        stack.append((left.right, right.left))

    return True