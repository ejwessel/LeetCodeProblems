# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # no items to rotate
        if head is None:
            return None

        size = 0
        c = head
        while c is not None:
            size += 1
            c = c.next

        k = k % size

        # in order for there to be a rotation there must be a value for k
        if k is 0:
            return head

        e = head
        while (k - 1) > 0:
            e = e.next
            k -= 1

        s = head
        tail = None

        while e.next is not None:
            tail = s
            s = s.next
            e = e.next

        # it's possible the list is too short that tail is never initialized
        if tail is not None:
            tail.next = e.next

        # we need to be careful because it possible to create a circular LL
        if head is not e:
            e.next = head
            head = s

        return head

def getListRepresentation(head):
    output = []
    c = head
    while c is not None:
        output.append(c.val)
        c = c.next
    return output

if __name__ == "__main__":
    sol = Solution()

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2
    new_head = sol.rotateRight(node_1, 2)
    output = getListRepresentation(new_head)
    assert output == [1, 2]


    # Test 8
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    output = getListRepresentation(node_1)

    new_head = sol.rotateRight(node_1, 1)
    output = getListRepresentation(new_head)
    assert output == [4, 1, 2, 3]

    # Test 7
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2
    output = getListRepresentation(node_1)

    new_head = sol.rotateRight(node_1, 0)
    output = getListRepresentation(new_head)
    assert output == [1, 2]

    # Test 6
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2
    output = getListRepresentation(node_1)

    new_head = sol.rotateRight(node_1, 100)
    output = getListRepresentation(new_head)
    assert output == [1, 2]

    # Test 5
    node_1 = ListNode(1)
    output = getListRepresentation(node_1)

    new_head = sol.rotateRight(node_1, 100)
    output = getListRepresentation(new_head)
    assert output == [1]

    # Test 1
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    output = getListRepresentation(node_1)

    new_head = sol.rotateRight(node_1, 2)
    output = getListRepresentation(new_head)
    assert output == [4, 5, 1, 2, 3]

    # Test 2
    node_0 = ListNode(0)
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_0.next = node_1
    node_1.next = node_2
    output = getListRepresentation(node_0)

    new_head = sol.rotateRight(node_0, 4)
    output = getListRepresentation(new_head)
    assert output == [2, 0, 1]

    # Test 3
    new_head = sol.rotateRight(None, 5)
    output = getListRepresentation(new_head)
    assert output == []

    # Test 4
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    output = getListRepresentation(node_1)

    new_head = sol.rotateRight(node_1, 6)
    output = getListRepresentation(new_head)
    assert output == [3, 4, 1, 2]


