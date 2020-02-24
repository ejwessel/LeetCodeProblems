# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        copy_nodes = {}
        current = head
        # discover nodes
        while current:
            copy_nodes[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            if current.next is not None:
                copy_nodes[current].next = copy_nodes[current.next]
            if current.random is not None:
                copy_nodes[current].random = copy_nodes[current.random]
            current = current.next

        return copy_nodes[head]

def printTraverse(head: 'Node'):
    output = []
    current = head
    while current is not None:
        output.append(current.val)
        current = current.next
    return output

if __name__ == "__main__":
    node_7 = Node(7)
    node_13 = Node(13)
    node_10 = Node(10)
    node_11 = Node(11)
    node_1 = Node(1)
    node_7.next = node_13
    node_13.next = node_11
    node_13.random = node_7
    node_11.next = node_10
    node_11.random = node_1
    node_10.next = node_1
    node_10.random = node_11
    output = printTraverse(node_7)
    sol = Solution()
    result = sol.copyRandomList(node_7)
    output = printTraverse(result)
    assert output == [7, 13, 11, 10, 1]

    node_1 = Node(1)
    node_2 = Node(2)
    node_1.next = node_2
    node_1.random = node_2
    node_2.random = node_2
    output = printTraverse(node_1)
    sol = Solution()
    result = sol.copyRandomList(node_1)
    output = printTraverse(result)
    assert output == [1, 2]

    result = sol.copyRandomList(None)
    output = printTraverse(result)
    assert output == []

