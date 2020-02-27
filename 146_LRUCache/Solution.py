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
        self.linkedlist = LinkedList()
        self.nodes = {}

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass

if __name__ == "__main__":
    linked_list = LinkedList()
    new_node_5 = Node(5)
    linked_list.insertHead(new_node_5)
    new_node_4 = Node(4)
    linked_list.insertHead(new_node_4)
    new_node_3 = Node(3)
    linked_list.insertHead(new_node_3)
    new_node_1 = Node(1)
    linked_list.insertHead(new_node_1)
    output = print_linkedlist(linked_list.head)
    assert output == [1, 3, 4, 5]

    node_removed = linked_list.removeTail()
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
    output = print_linkedlist(linked_list.head)
    assert output == []

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

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)