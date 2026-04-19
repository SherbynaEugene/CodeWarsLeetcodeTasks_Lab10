'''Binary Tree Traversal: Pre-order, In-order, Post-order.'''


# Pre-order traversal
def pre_order(node):
    '''Pre-order traversal of a binary tree.'''
    if node is None:
        return []
    root = node.data
    return [root] + pre_order(node.left) + pre_order(node.right)

# In-order traversal
def in_order(node):
    '''In-order traversal of a binary tree.'''
    if node is None:
        return []
    root = node.data
    return in_order(node.left) + [root] + in_order(node.right)

# Post-order traversal
def post_order(node):
    '''Post-order traversal of a binary tree.'''
    if node is None:
        return []
    root = node.data
    return post_order(node.left) + post_order(node.right) + [root]
