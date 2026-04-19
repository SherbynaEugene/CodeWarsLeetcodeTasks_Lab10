'''Sort Binary Tree by Levels: Return values of a binary tree sorted by levels.'''

from collections import deque

def tree_by_levels(node):
    '''Return values of a binary tree sorted by levels.'''
    if node is None:
        return []

    result = []
    queue = deque([node])

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result
