# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = None
        tail = head
        # handle logic when combining the lists
        while (l1 is not None) and (l2 is not None):
            # choose l1 over l2
            if l1.val <= l2.val:
                if head is None:
                    head = l1
                    tail = head
                else:
                    tail.next = l1
                    tail = tail.next
                # move head pointer of l1 to next node
                l1 = l1.next
            # Choose l2 over l1
            elif l2.val < l1.val:
                if head is None:
                    head = l2
                    tail = head
                else:
                    tail.next = l2
                    tail = tail.next
                # move head pointer of l1 to next node
                l2 = l2.next

        # handle when there are left overs in a list
        if l1 is not None:
            if head is None:
                head = l1
            else:
                tail.next = l1
        if l2 is not None:
            if head is None:
                head = l2
            else:
                tail.next = l2
        return head

def print_list(list_to_print):
    current = list_to_print
    while current is not None:
        print(current.val)
        current = current.next

def ll_from_list(list_to_convert):
    head = None
    current = head
    for item in list_to_convert:
        newNode = ListNode(item)
        if head is None:
            head = newNode
            current = head
        else:
            current.next = newNode
            current = current.next
    return head


if __name__ == "__main__":
    list1 = ll_from_list([1, 2, 4])
    list2 = ll_from_list([1, 3, 4])
    result = Solution().mergeTwoLists(list1, list2)
    print_list(result)
    print()

    list1 = ll_from_list([])
    list2 = ll_from_list([1, 3, 4])
    result = Solution().mergeTwoLists(list1, list2)
    print_list(result)
    print()

    list2 = ll_from_list([])
    list1 = ll_from_list([1, 3, 4])
    result = Solution().mergeTwoLists(list1, list2)
    print_list(result)
    print()

    list1 = ll_from_list([9, 13, 15])
    list2 = ll_from_list([1, 3, 4])
    result = Solution().mergeTwoLists(list1, list2)
    print_list(result)
    print()

    list1 = ll_from_list([9, 9, 9])
    list2 = ll_from_list([9, 9, 9])
    result = Solution().mergeTwoLists(list1, list2)
    print_list(result)
    print()

    list1 = ll_from_list([])
    list2 = ll_from_list([])
    result = Solution().mergeTwoLists(list1, list2)
    print_list(result)
    print()