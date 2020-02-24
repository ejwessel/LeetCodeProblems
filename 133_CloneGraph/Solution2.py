from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0):
        self.val = val
        self.neighbors = []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        copy_nodes = {}
        seen = {node}
        queue = deque()
        queue.append(node)

        # create all node representations mapped to their copy
        while queue:
            current = queue.popleft()
            copy_nodes[current] = Node(current.val)
            for neighbor in current.neighbors:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)

        seen = {node}
        queue = deque()
        queue.append(node)

        # link nodes
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                copy_nodes[current].neighbors.append(copy_nodes[neighbor])
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)

        return copy_nodes[node]


def bfs_output(node: Node):
    seen_set = set()
    output = []
    queue = deque()
    queue.append(node)
    seen_set.add(node)

    while queue:
        current = queue.popleft()
        output.append(current.val)
        for neighbor in current.neighbors:
            if neighbor not in seen_set:
                seen_set.add(neighbor)
                queue.append(neighbor)
    return output


if __name__ == "__main__":
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]
    sol = Solution()
    cloned_root = sol.cloneGraph(node_1)
    output = bfs_output(cloned_root)
    assert output == [1, 2, 4, 3]

    node_1 = Node(1)
    node_2 = Node(2)
    node_1.neighbors = [node_2]
    node_2.neighbors = [node_1]
    sol2 = Solution()
    cloned_root = sol2.cloneGraph(node_1)
    output = bfs_output(cloned_root)
    assert output == [1, 2]

    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    node_e = Node('E')
    node_f = Node('F')
    node_a.neighbors = [node_b, node_d]
    node_b.neighbors = [node_a, node_c, node_e]
    node_c.neighbors = [node_b, node_e, node_d]
    node_d.neighbors = [node_a, node_c, node_f]
    node_e.neighbors = [node_b, node_c, node_f]
    node_f.neighbors = [node_e, node_d]
    sol = Solution()
    cloned_root = sol.cloneGraph(node_a)
    output = bfs_output(cloned_root)
    assert output == ['A', 'B', 'D', 'C', 'E', 'F']
