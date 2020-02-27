class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertHead(self, new_node: Node):
        '''
        inserts a new node into the linked list
        :param new_node:
        :return:
        '''
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # increase size
        self.size += 1

    def removeTail(self):
        '''
        removes the tail and returns the removed element
        :return: the removed element
        '''
        # if there is nothing to remove
        if self.size == 0:
            return None
        # if there is size 1 then handle head and tail assignments
        elif self.size == 1:
            element_to_remove = self.tail
            element_to_remove.prev = None
            self.head = None
            self.tail = None
            self.size -= 1
            return element_to_remove
        # if there are more than 1 element handle assignments
        else:
            element_to_remove = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            element_to_remove.prev = None
            self.size -= 1
            return element_to_remove


class Bidict:
    def __init__(self):
        self.key_to_val = {}
        self.val_to_key = {}

    def insert(self, key, val):
        self.remove_key(key)
        self.key_to_val[key] = val
        self.val_to_key[val] = key

    def remove_key(self, key):
        """
        remove should be unidirectional
        """
        if key not in self.key_to_val:
            return
        value = self.key_to_val[key]
        del self.key_to_val[key]
        del self.val_to_key[value]


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = LinkedList()
        self.nodes = Bidict()

    def get(self, key: int) -> int:
        """
        no updates to keys need to happen here. The queried node (should it exist) should be moved to the front
        :param key:
        :return:
        """
        if key not in self.nodes.key_to_val:
            return -1
        node_to_move = self.nodes.key_to_val[key]

        if node_to_move == self.linked_list.head:
            return node_to_move.val
        elif node_to_move == self.linked_list.tail:
            self.linked_list.tail = self.linked_list.tail.prev
            self.linked_list.tail.next = None
            node_to_move.prev = None
            self.linked_list.size -= 1
            self.linked_list.insertHead(node_to_move)
            return node_to_move.val
        else:
            # link prev and next together
            node_to_move.prev.next = node_to_move.next
            node_to_move.next.prev = node_to_move.prev
            # disconnect the node
            node_to_move.next = None
            node_to_move.prev = None
            self.linked_list.size -= 1
            # insert it into the beginning
            self.linked_list.insertHead(node_to_move)
            return node_to_move.val

    def put(self, key: int, value: int) -> None:
        """
        The queried node (should it exist) value will be updated and moved to the front
        If the node doesn't exist then it will be added to the front.
        If the length of the list goes over capacity then the last node is evicted
        :param key:
        :param value:
        :return:
        """
        if key in self.nodes.key_to_val:
            node_to_move = self.nodes.key_to_val[key]
            node_to_move.val = value
            self.nodes.insert(key, node_to_move)

            # move the node to the beginning
            # if this node is a the beginning do nothing
            if node_to_move == self.linked_list.head:
                return
            # if the node is at the end update the tail
            elif node_to_move == self.linked_list.tail:
                self.linked_list.tail = self.linked_list.tail.prev
                self.linked_list.tail.next = None
                node_to_move.prev = None
                self.linked_list.size -= 1
                self.linked_list.insertHead(node_to_move)
            # if the node is anywhere else
            else:
                # link prev and next together
                node_to_move.prev.next = node_to_move.next
                node_to_move.next.prev = node_to_move.prev
                # disconnect the node
                node_to_move.next = None
                node_to_move.prev = None
                self.linked_list.size -= 1
                # insert it into the beginning
                self.linked_list.insertHead(node_to_move)
        # if the the key value pair is new
        else:
            # insert
            new_node = Node(value)
            self.nodes.insert(key, new_node)
            self.linked_list.insertHead(new_node)

            # check if we need to evict the last node
            if self.linked_list.size > self.capacity:
                removed_node = self.linked_list.removeTail()
                key_to_remove = self.nodes.val_to_key[removed_node]
                self.nodes.remove_key(key_to_remove)


def print_linkedlist(head: Node):
    output = []
    current = head
    while current:
        output.append(current.val)
        current = current.next
    return output


def linkedlists_tests():
    linked_list = LinkedList()
    assert linked_list.size == 0
    new_node_5 = Node(5)
    linked_list.insertHead(new_node_5)
    new_node_4 = Node(4)
    linked_list.insertHead(new_node_4)
    new_node_3 = Node(3)
    linked_list.insertHead(new_node_3)
    new_node_1 = Node(1)
    linked_list.insertHead(new_node_1)
    assert linked_list.tail == new_node_5
    assert linked_list.head == new_node_1
    assert linked_list.size == 4
    output = print_linkedlist(linked_list.head)
    assert output == [1, 3, 4, 5]

    node_removed = linked_list.removeTail()
    assert linked_list.tail == new_node_4
    assert linked_list.head == new_node_1
    assert node_removed == new_node_5
    output = print_linkedlist(linked_list.head)
    assert output == [1, 3, 4]

    node_removed = linked_list.removeTail()
    assert node_removed == new_node_4
    node_removed = linked_list.removeTail()
    assert node_removed == new_node_3
    node_removed = linked_list.removeTail()
    assert node_removed == new_node_1
    node_removed = linked_list.removeTail()  # won't provide anything if nothing to remove
    assert node_removed is None
    assert linked_list.size == 0
    assert linked_list.head is None
    assert linked_list.tail is None
    output = print_linkedlist(linked_list.head)
    assert output == []


def bidict_tests():
    bidict = Bidict()
    bidict.insert(5, "hello")
    assert 5 in bidict.key_to_val
    assert 6 not in bidict.key_to_val
    assert "hello" in bidict.val_to_key
    assert "helloo" not in bidict.val_to_key
    bidict.remove_key(5)
    assert 5 not in bidict.key_to_val
    assert "hello" not in bidict.val_to_key
    bidict.remove_key(6)
    assert 56 not in bidict.key_to_val
    bidict.insert(1, 1)
    bidict.insert(2, 2)
    bidict.insert(3, 3)
    bidict.insert(4, 4)
    bidict.insert(1, 5)
    assert 1 in bidict.key_to_val
    assert 2 in bidict.key_to_val
    assert 3 in bidict.key_to_val
    assert 4 in bidict.key_to_val
    assert 1 not in bidict.val_to_key
    assert 2 in bidict.val_to_key
    assert 3 in bidict.val_to_key
    assert 4 in bidict.val_to_key
    assert 5 in bidict.val_to_key


def lrucache_tests():
    lru_cache = LRUCache(4)
    assert lru_cache.get(5) == -1
    lru_cache.put(5, 4)
    assert lru_cache.get(5) == 4
    lru_cache.put(5, 3)
    assert lru_cache.get(5) == 3
    size = lru_cache.linked_list.size
    assert size == 1
    lru_cache.put(3, 2)
    assert lru_cache.get(3) == 2
    size = lru_cache.linked_list.size
    assert size == 2
    output = print_linkedlist(lru_cache.linked_list.head)
    assert output == [2, 3]
    lru_cache.get(5)
    output = print_linkedlist(lru_cache.linked_list.head)
    assert output == [3, 2]

    lru_cache = LRUCache(4)
    lru_cache.put(1, 5)
    lru_cache.put(2, 4)
    lru_cache.put(3, 3)
    lru_cache.put(4, 2)
    output = print_linkedlist(lru_cache.linked_list.head)
    assert output == [2, 3, 4, 5]
    lru_cache.put(5, 1)
    output = print_linkedlist(lru_cache.linked_list.head)
    assert output == [1, 2, 3, 4]
    assert lru_cache.linked_list.size == 4

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    output = print_linkedlist(cache.linked_list.head)
    assert output == [1, 2]
    cache.put(3, 3);  # evicts key 2
    output = print_linkedlist(cache.linked_list.head)
    assert output == [3, 1]
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    output = print_linkedlist(cache.linked_list.head)
    assert output == [4, 3]
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(10)
    commands = ["put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
                "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put",
                "get",
                "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put",
                "put",
                "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get",
                "put",
                "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put",
                "put",
                "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put",
                "put",
                "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]

    data = [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
            [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3],
            [10, 11], [8],
            [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
            [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26],
            [8, 17],
            [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
            [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
            [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1],
            [2, 2],
            [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

    output = []
    for command_i in range(len(commands)):
        if commands[command_i] == "put":
            key, value = data[command_i]
            cache.put(key, value)
            output.append(None)
        else:
            key = data[command_i][0]
            value = cache.get(key)
            output.append(value)

    # print(output)
    assert output == [None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5, -1,
                      12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1,
                      24, None, None, 18, None, None, None, None, -1, None, None, 18, None, None, -1, None, None, None,
                      None, None, 18, None, None, -1, None, 4, 29, 30, None, 12, -1, None, None, None, None, 29, None,
                      None, None, None, 17, 22, 18, None, None, None, -1, None, None, None, 20, None, None, None, -1,
                      18, 18, None, None, None, None, 20, None, None, None, None, None, None, None]


if __name__ == "__main__":
    linkedlists_tests()
    bidict_tests()
    lrucache_tests()
