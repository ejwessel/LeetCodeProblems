# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.head = None

    def treeToDoublyList(self, root: Node) -> Node:
        self.treeToDoublyListHelper(root)
        current = self.head
        tail = None
        while current is not None:
            tail = current
            current = current.right

        # can only link if there is an element to link
        if self.head is not None:
            tail.right = self.head
            self.head.left = tail

        return self.head

    def treeToDoublyListHelper(self, root: Node):
        if root is None:
            return

        self.treeToDoublyListHelper(root.left)
        self.treeToDoublyListHelper(root.right)
        # unlink the node and prepare for insertion
        root.left = None
        root.right = None
        self.insertSort(root)

    def insertSort(self, new_node):
        # handle if this is the first element
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            tail = None
            while current is not None and new_node.val > current.val:
                tail = current
                current = current.right

            # we're at the insertion spot
            # handle insertion at head, tail, internal
            if current is self.head:
                new_node.right = self.head
                self.head.left = new_node
                self.head = new_node
            elif current is None:
                tail.right = new_node
                new_node.left = tail
            else:
                # set node up to point to prev and next
                new_node.right = current
                new_node.left = current.left
                # set prev and next to point to new node
                new_node.left.right = new_node
                new_node.right.left = new_node


def linkedListOutput(head: Node):
    output = []
    current = head
    seen = set()
    while current is not None and current not in seen:
        seen.add(current)
        output.append(current.val)
        current = current.right
    return output


if __name__ == "__main__":
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    node_a.right = node_b
    node_b.right = node_c
    node_c.right = node_d
    output = linkedListOutput(node_a)
    assert output == ['A', 'B', 'C', 'D']

    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_6 = Node(6)
    node_7 = Node(7)
    node_8 = Node(8)
    node_9 = Node(9)
    node_1.left = node_3
    node_1.right = node_2
    node_3.left = node_4
    node_3.right = node_5
    node_2.left = node_6
    node_2.right = node_7
    node_4.left = node_8
    node_4.right = node_9
    sol = Solution()
    head = sol.treeToDoublyList(node_1)
    output = linkedListOutput(head)
    assert output == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    node_4 = Node(4)
    node_2 = Node(2)
    node_5 = Node(5)
    node_1 = Node(1)
    node_3 = Node(3)

    node_4.left = node_2
    node_4.right = node_5
    node_2.left = node_1
    node_2.right = node_3

    sol = Solution()
    head = sol.treeToDoublyList(node_4)
    output = linkedListOutput(head)
    assert output == [1, 2, 3, 4, 5]

    sol = Solution()
    head = sol.treeToDoublyList(None)
    output = linkedListOutput(head)
    assert output == []

    sol = Solution()
    node_1 = Node(1)
    head = sol.treeToDoublyList(node_1)
    output = linkedListOutput(head)
    assert output == [1]

