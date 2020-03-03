from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MinHeap:
    def __init__(self):
        self.capacity = 100
        self.heap = [None] * self.capacity
        self.size = 0

    def get_parent(self, index):
        return (index - 1) // 2

    def insert(self, new_node):
        self.heap[self.size] = new_node
        # heapify up
        current_idx = self.size
        while current_idx != 0:
            parent = self.get_parent(current_idx)
            if self.heap[current_idx].val < self.heap[parent].val:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[current_idx]
                self.heap[current_idx] = temp
                current_idx = parent
            else:
                break

        # increase size
        self.size += 1
        # handle if we're at capacity
        if self.size + 1 == self.capacity:
            list_addendum = [None] * self.capacity
            self.heap += list_addendum
            self.capacity *= 2

    def getMin(self):
        if self.size <= 0:
            return None

        # handle getting element
        temp = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap[self.size - 1] = None
        self.size -= 1
        # element is removed and ready to be returned
        min_element = temp

        # down heap from top
        current_idx = 0
        swapped = True
        while swapped:
            left_idx = current_idx * 2 + 1
            right_idx = current_idx * 2 + 2

            idx_to_compare = None
            if left_idx < self.size and right_idx < self.size:
                if self.heap[left_idx].val <= self.heap[right_idx].val:
                    idx_to_compare = left_idx
                elif self.heap[right_idx].val < self.heap[left_idx].val:
                    idx_to_compare = right_idx
            elif left_idx < self.size:
                idx_to_compare = left_idx
            elif right_idx < self.size:
                idx_to_compare = right_idx

            # do the comparision to determine if heapify
            if idx_to_compare is not None and self.heap[idx_to_compare].val < self.heap[current_idx].val:
                temp = self.heap[idx_to_compare]
                self.heap[idx_to_compare] = self.heap[current_idx]
                self.heap[current_idx] = temp
                current_idx = idx_to_compare
            else:
                swapped = False

        return min_element


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = MinHeap()
        # add the linked lists to the heap
        for list in lists:
            if list is None:
                continue
            heap.insert(list)

        head = None
        tail = None
        while heap.size > 0:
            next_element = heap.getMin()
            remaining_head = next_element.next
            next_element.next = None
            if remaining_head is not None:
                heap.insert(remaining_head)
            if head is None:
                head = next_element
                tail = head
            else:
                tail.next = next_element
                tail = tail.next

        return head


def print_linked_list(head: ListNode):
    output = []
    current = head
    while current:
        output.append(current.val)
        current = current.next
    return output


def create_linked_list(list):
    head = None
    tail = None
    for item in list:
        if head is None:
            head = ListNode(item)
            tail = head
        else:
            tail.next = ListNode(item)
            tail = tail.next
    return head


if __name__ == "__main__":
    # minHeap = MinHeap()
    # minHeap.insert(1)
    # minHeap.insert(9)
    # minHeap.insert(6)
    # minHeap.insert(4)
    # minHeap.insert(0)
    # minHeap.insert(-1)
    # minHeap.insert(-1)
    # print(minHeap.heap)
    #
    # minHeap = MinHeap()
    # minHeap.insert(1)
    # minHeap.insert(9)
    # minHeap.insert(6)
    # minHeap.insert(4)
    # minHeap.insert(0)
    # minHeap.insert(-1)
    # minHeap.insert(-1)
    # result = minHeap.getMin()
    # print(result)
    # result = minHeap.getMin()
    # print(result)
    # result = minHeap.getMin()
    # print(result)
    # result = minHeap.getMin()
    # print(result)
    # result = minHeap.getMin()
    # print(result)
    # result = minHeap.getMin()
    # print(result)
    # result = minHeap.getMin()
    # print(result)
    # result = minHeap.getMin()
    # print(result)
    # result = minHeap.getMin()
    # print(result)

    list_of_lists = [[-8, -7, -6, -3, -2, -2, 0, 3], [-10, -6, -4, -4, -4, -2, -1, 4], [-10, -9, -8, -8, -6],
                     [-10, 0, 4]]
    linked_lists = []
    for list in list_of_lists:
        new_ll = create_linked_list(list)
        linked_lists.append(new_ll)
    sol = Solution()
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == [-10, -10, -10, -9, -8, -8, -8, -7, -6, -6, -6, -4, -4, -4, -3, -2, -2, -2, -1, 0, 0, 3, 4, 4]
    print(output)

    node1_1 = ListNode(1)
    node1_2 = ListNode(4)
    node1_3 = ListNode(5)
    node1_1.next = node1_2
    node1_2.next = node1_3
    output = print_linked_list(node1_1)
    assert output == [1, 4, 5]

    node2_1 = ListNode(1)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    node2_1.next = node2_2
    node2_2.next = node2_3
    output = print_linked_list(node2_1)
    assert output == [1, 3, 4]

    node3_1 = ListNode(2)
    node3_2 = ListNode(6)
    node3_1.next = node3_2
    output = print_linked_list(node3_1)
    assert output == [2, 6]

    linked_lists = [node1_1, node2_1, node3_1]
    sol = Solution()
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == [1, 1, 2, 3, 4, 4, 5, 6]

    node1_2 = ListNode(2)
    node1_3 = ListNode(5)
    linked_lists = [node1_2, None, node1_3]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == [2, 5]

    node1_3 = ListNode(5)
    linked_lists = [None, node1_3]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == [5]

    linked_lists = [None, None]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == []

    linked_lists = [None]
    result = sol.mergeKLists(linked_lists)
    output = print_linked_list(result)
    assert output == []

