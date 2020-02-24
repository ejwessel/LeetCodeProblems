from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        copy_start = None
        copy_nodes = {}  # maps key to copy node representation
        seen_set = {node}  # don't revisit nodes already seen
        queue = deque()
        queue.append(node)

        while queue:
            current = queue.popleft()

            # if we're dealing with the first node
            if not copy_start:
                new_copy = Node(current.val)
                copy_nodes[current.val] = new_copy
                copy_start = new_copy

            # visit all the neighbors of the current node
            for neighbor in current.neighbors:
                # create new node if needed
                if neighbor.val not in copy_nodes:
                    new_copy = Node(neighbor.val)
                    copy_nodes[neighbor.val] = new_copy

                # link the node
                current_copy = copy_nodes[current.val]
                neighbor_copy = copy_nodes[neighbor.val]
                current_copy.neighbors.append(neighbor_copy)

                # determine if neighbor needs to be added to the queue
                if neighbor not in seen_set:
                    seen_set.add(neighbor)
                    queue.append(neighbor)

        return copy_start


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

    # node_1 = Node(1)
    # node_2 = Node(2)
    # node_1.neighbors = [node_2]
    # node_2.neighbors = [node_1]
    # sol2 = Solution()
    # cloned_root = sol2.cloneGraph(node_1)
    # output = bfs_output(cloned_root)
    # assert output == [1, 2]
