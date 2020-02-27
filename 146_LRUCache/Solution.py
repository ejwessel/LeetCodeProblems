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


def print_linkedlist(head: Node):
    output = []
    current = head
    while current:
        output.append(current.val)
        current = current.next
    return output

class Bidict:
    def __init__(self):
        self.key_to_val = {}
        self.val_to_key = {}

    def insert(self, key, val):
        self.key_to_val[key] = val
        self.val_to_key[val] = key

    def remove_key(self, key):
        if key not in self.key_to_val:
            return
        value = self.key_to_val[key]
        del self.key_to_val[key]
        del self.val_to_key[value]

    def remove_val(self, val):
        if val not in self.val_to_key:
            return
        key = self.val_to_key[val]
        del self.val_to_key[val]
        del self.key_to_val[key]

    def contains_key(self, key):
        return key in self.key_to_val

    def contains_val(self, val):
        return val in self.val_to_key


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = LinkedList()
        self.nodes = Bidict()

    def get(self, key: int) -> int:
        if not self.nodes.contains_key(key):
            return -1
        node_to_move = self.nodes.key_to_val[key]

        if node_to_move == self.linked_list.head:
            return node_to_move.val
        elif node_to_move == self.linked_list.tail:
            self.linked_list.tail = self.linked_list.tail.prev
            self.linked_list.tail.next = None
            node_to_move.prev = None
            self.linked_list.insertHead(node_to_move)
            return node_to_move.val
        else:
            # link prev and next together
            node_to_move.prev.next = node_to_move.next
            node_to_move.next.prev = node_to_move.prev
            # disconnect the node
            node_to_move.next = None
            node_to_move.prev = None
            # insert it into the beginning
            self.linked_list.insertHead(node_to_move)
            return node_to_move.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes.key_to_val:
            # update the value
            node_to_move = self.nodes.key_to_val[key]
            node_to_move.val = value

            # move the node to the beginning
            # if this node is a the beginning do nothing
            if node_to_move == self.linked_list.head:
                return
            # if the node is at the end update the tail
            elif node_to_move == self.linked_list.tail:
                self.linked_list.tail = self.linked_list.tail.prev
                self.linked_list.tail.next = None
                node_to_move.prev = None
                self.linked_list.insertHead(node_to_move)
            # if the node is anywhere else
            else:
                # link prev and next together
                node_to_move.prev.next = node_to_move.next
                node_to_move.next.prev = node_to_move.prev
                # disconnect the node
                node_to_move.next = None
                node_to_move.prev = None
                # insert it into the beginning
                self.linked_list.insertHead(node_to_move)
        else:
            # insert
            new_node = Node(value)
            self.nodes.insert(key, new_node)
            self.linked_list.insertHead(new_node)

            # check if we need to evict
            if self.linked_list.size > self.capacity:
                removed_node = self.linked_list.removeTail()
                self.nodes.remove_val(removed_node)

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
    node_removed = linked_list.removeTail() # won't provide anything if nothing to remove
    assert node_removed is None
    assert linked_list.size == 0
    assert linked_list.head is None
    assert linked_list.tail is None
    output = print_linkedlist(linked_list.head)
    assert output == []

def bidict_tests():
    bidict = Bidict()
    bidict.insert(5, "hello")
    contains = bidict.contains_key(5)
    assert contains
    contains = bidict.contains_key(6)
    assert not contains
    contains = bidict.contains_val("hello")
    assert contains
    contains = bidict.contains_val("hello0")
    assert not contains
    bidict.remove_key(5)
    contains = bidict.contains_key(5)
    assert not contains
    contains = bidict.contains_val("hello")
    assert not contains
    bidict.remove_key(6)
    contains = bidict.contains_key(56)
    assert not contains


if __name__ == "__main__":

    linkedlists_tests()
    bidict_tests()

    lru_cache = LRUCache(4)
    result = lru_cache.get(5)
    assert result == -1
    lru_cache.put(5, 4)
    result = lru_cache.get(5)
    assert result == 4
    lru_cache.put(5, 3)
    result = lru_cache.get(5)
    assert result == 3
    size = lru_cache.linked_list.size
    assert size == 1
    lru_cache.put(3, 2)
    result = lru_cache.get(3)
    assert result == 2
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

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    output = print_linkedlist(cache.linked_list.head)
    assert output == [1, 2]
    cache.put(3, 3); # evicts key 2
    output = print_linkedlist(cache.linked_list.head)
    assert output == [3, 1]
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    output = print_linkedlist(cache.linked_list.head)
    assert output == [4, 3]
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)