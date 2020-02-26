# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = [(root, 'left')]

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # set the stack up if needed
        while self.stack[-1][1] == 'left':
            current, direction = self.stack.pop()
            if current is None:
                continue
            self.stack.append((current, 'right'))
            self.stack.append((current.left, 'left'))

        # top should be right now and we can fetch it
        if self.stack[-1][1] == 'right':
            current, direction = self.stack.pop()
            # make sure to add the right node
            self.stack.append((current.right, 'left'))
            return current.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        # remove any dummy nodes on top
        while self.stack and self.stack[-1][0] is None:
            self.stack.pop()
        return len(self.stack) > 0

if __name__ == "__main__":
    root = TreeNode(1)
    obj = BSTIterator(root)
    next_val = obj.next()
    # has_next = obj.hasNext()
    assert next_val == 1
    # assert not has_next


    node_7 = TreeNode(7)
    node_3 = TreeNode(3)
    node_15 = TreeNode(15)
    node_9 = TreeNode(9)
    node_20 = TreeNode(20)
    node_7.left = node_3
    node_7.right = node_15
    node_15.left = node_9
    node_15.right = node_20
    obj = BSTIterator(node_7)

    next_val = obj.next()
    assert next_val == 3
    has_next = obj.hasNext()
    assert has_next
    next_val = obj.next()
    assert next_val == 7
    has_next = obj.hasNext()
    assert has_next
    next_val = obj.next()
    assert next_val == 9
    has_next = obj.hasNext()
    assert has_next
    next_val = obj.next()
    assert next_val == 15
    has_next = obj.hasNext()
    assert has_next
    has_next = obj.hasNext()
    assert has_next
    has_next = obj.hasNext()
    assert has_next
    has_next = obj.hasNext()
    assert has_next
    next_val = obj.next()
    assert next_val == 20
    has_next = obj.hasNext()
    assert not has_next
    has_next = obj.hasNext()
    assert not has_next
