# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_1:
    def __init__(self):
        self._base = 10

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        assert(l1 is not None)
        assert(l2 is not None)

        val1 = int_rep(l1)
        val2 = int_rep(l2)

        sum = val1 + val2
        summed_list = rev_list_rep(sum)

        return summed_list

    def test(self, num1, num2):
        """
        Given two numbers in integer format , adds them together
        :param num1: int
        :param num2: int
        :return: int format
        """
        list1 = rev_list_rep(num1)
        list2 = rev_list_rep(num2)

        print("List 1: ")
        current_element = list1
        while(current_element) is not None:
            print(str(current_element.val) + " > ", end='')
            current_element = current_element.next
        print("")
        print("List 2:")
        current_element = list2
        while (current_element) is not None:
            print(str(current_element.val) + " > ", end='')
            current_element = current_element.next

        sol = Solution_1().addTwoNumbers(list1, list2)

        print("")
        print("Summed list:")
        current_element = sol
        while (current_element) is not None:
            print(str(current_element.val) + " > ", end='')
            current_element = current_element.next

        print("\n")
        return int_rep(sol)

class Solution_2:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        assert (l1 is not None)
        assert (l2 is not None)

        l1_pos = l1
        l2_pos = l2
        remainder = 0

        summed_list = None
        summed_list_pos = None

        while l1_pos is not None and l2_pos is not None:
            summed_val = l1_pos.val + l2_pos.val + remainder
            digit = int(summed_val % 10)
            remainder = int(summed_val / 10)

            #if we're just starting
            if summed_list is None:
                summed_list = ListNode(digit)
                summed_list_pos = summed_list
            else:
                summed_list_pos.next = ListNode(digit)
                summed_list_pos = summed_list_pos.next

            #move the list positions
            l1_pos = l1_pos.next
            l2_pos = l2_pos.next

        #if it's l1 that's not empty we need to handle remaining elements
        while l1_pos is not None:
            summed_val = l1_pos.val + remainder
            digit = int(summed_val % 10)
            remainder = int(summed_val / 10)
            summed_list_pos.next = ListNode(digit)
            summed_list_pos = summed_list_pos.next
            l1_pos = l1_pos.next


        #if it's l2 that's not empty we need to handle remaining elements
        while l2_pos is not None:
            summed_val = l2_pos.val + remainder
            digit = int(summed_val % 10)
            remainder = int(summed_val / 10)
            summed_list_pos.next = ListNode(digit)
            summed_list_pos = summed_list_pos.next
            l2_pos = l2_pos.next

        #handle remainder
        if remainder is not 0:
            summed_list_pos.next = ListNode(remainder)

        return summed_list

    def test(self, num1, num2):
        """
        Given two numbers in integer format , adds them together
        :param num1: int
        :param num2: int
        :return: int format
        """
        list1 = rev_list_rep(num1)
        list2 = rev_list_rep(num2)

        sum_list = self.addTwoNumbers(list1, list2)

        print(int_rep(sum_list))

        return int_rep(sum_list)

def int_rep(list):
    """
    Creates an integer representation given a list
    :param list:
    :return:
    """
    value_str = ""

    current_node = list
    while current_node is not None:
        value_str = str(current_node.val) + value_str[0:]
        current_node = current_node.next

    return int(value_str)

def rev_list_rep(value):
    """
    creates a list repesentation given a positive integer
    :param value:
    :return:
    """
    # turn it into a string
    reversed_notation = str(value)[::-1]
    list_representation = None
    last_element = None
    for c in reversed_notation:
        if list_representation is None:
            list_representation = ListNode(int(c))
            last_element = list_representation
        else:
            last_element.next = ListNode(int(c))
            last_element = last_element.next

    return list_representation

if __name__ == "__main__":

    print("Solution 1 =================================")
    assert(Solution_1().test(342, 465) == 807) #default test case
    assert(Solution_1().test(000, 000) == 0) #all zeroes
    assert(Solution_1().test(1, 400) == 401) #unequal sizes
    assert(Solution_1().test(400, 1) == 401) #reversed unequal sizes
    assert(Solution_1().test(9, 1) == 10) #remainder carry

    print("Solution 2 =================================")
    assert (Solution_2().test(342, 465) == 807)  # default test case
    assert (Solution_2().test(000, 000) == 0)  # all zeroes
    assert (Solution_2().test(1, 400) == 401)  # unequal sizes
    assert (Solution_2().test(400, 1) == 401)  # reversed unequal sizes
    assert (Solution_2().test(9, 1) == 10)  # remainder carry

    #Solution 1 is not optimal:
    #1. Convert reversed list into integer
    #   O(n) traversal through list
    #   O(n) reverse list
    #2. Sum integers
    #   O(1)
    #3. Convert Summed Integers back into reverse list notation
    #   O(m) new list size

    # O(max(2n, m))

    #Solution 2 is more optimal:
    #makes 1 pass through the list and adds all elements
    # O(max(len(list1, len(list2))