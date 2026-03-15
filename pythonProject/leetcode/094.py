root = [1, 1, 2, 3]


def preOrder(root):
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)


print(preOrder(root))
