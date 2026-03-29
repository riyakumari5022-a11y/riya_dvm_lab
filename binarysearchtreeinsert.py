def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root