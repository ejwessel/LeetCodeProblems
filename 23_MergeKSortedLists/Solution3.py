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
        self.next_idx = 0

    def get_parent(self, index):
        if index % 2 == 0:
            return (index - 2) // 2
        else:
            return (index - 1) // 2

    def insert(self, new_node):
        self.heap[self.next_idx] = new_node
        # heapify up
        current_idx = self.next_idx
        while current_idx != 0:
            parent = self.get_parent(current_idx)
            if self.heap[current_idx] < self.heap[parent]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[current_idx]
                self.heap[current_idx] = temp
                current_idx = parent
            else:
                break

        # update the pointer to the next available spot
        self.next_idx += 1
        # handle if we're at capacity
        if self.next_idx + 1 == self.capacity:
            list_addendum = [None] * self.capacity
            self.heap += list_addendum
            self.capacity *= 2

    def getMin(self):
        if self.next_idx <= 0:
            return None

        # handle getting element
        temp = self.heap[0]
        self.heap[0] = self.heap[self.next_idx - 1]
        self.heap[self.next_idx - 1] = temp
        self.heap[self.next_idx - 1] = None
        self.next_idx -= 1
        # element is removed and ready to be returned
        min_element = temp

        # down heap from top
        current_idx = 0
        swapped = True
        while swapped:
            left_idx = current_idx * 2 + 1
            right_idx = current_idx * 2 + 2

            if self.heap[left_idx] is None and self.heap[right_idx] is None:
                idx_to_compare = None
            elif self.heap[left_idx] is None:
                idx_to_compare = right_idx
            elif self.heap[right_idx] is None:
                idx_to_compare = left_idx
            else:
                if self.heap[left_idx] < self.heap[right_idx]:
                    idx_to_compare = left_idx
                elif self.heap[right_idx] < self.heap[left_idx]:
                    idx_to_compare = right_idx

            # do the comparision to determine if heapify
            if idx_to_compare is not None and self.heap[idx_to_compare] < self.heap[current_idx]:
                temp = self.heap[idx_to_compare]
                self.heap[idx_to_compare] = self.heap[current_idx]
                self.heap[current_idx] = temp
                current_idx = idx_to_compare
            else:
                swapped = False

        return min_element



class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass

def print_linked_list(head: ListNode):
    output = []
    current = head
    while current:
        output.append(current.val)
        current = current.next
    return output


if __name__ == "__main__":
    minHeap = MinHeap()
    minHeap.insert(1)
    minHeap.insert(9)
    minHeap.insert(6)
    minHeap.insert(4)
    minHeap.insert(0)
    minHeap.insert(-1)
    minHeap.insert(-1)
    print(minHeap.heap)

    minHeap = MinHeap()
    minHeap.insert(1)
    minHeap.insert(9)
    minHeap.insert(6)
    minHeap.insert(4)
    minHeap.insert(0)
    minHeap.insert(-1)
    minHeap.insert(-1)
    result = minHeap.getMin()
    print(result)
    result = minHeap.getMin()
    print(result)
    result = minHeap.getMin()
    print(result)
    result = minHeap.getMin()
    print(result)
    result = minHeap.getMin()
    print(result)
    result = minHeap.getMin()
    print(result)
    result = minHeap.getMin()
    print(result)
    result = minHeap.getMin()
    print(result)
    result = minHeap.getMin()
    print(result)
