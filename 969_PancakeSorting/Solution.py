from typing import List

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        '''
        Pancake Sorts a list
        :param A: the list to be sorted
        :return: the indices of the elements that were reversed at
        '''
        answer = []
        for i in reversed(range(len(A))):
            largest_idx = self.find_largest_element_idx(A, i)

            # place largest element at beginning
            left_portion = A[:largest_idx + 1]
            answer.append(largest_idx + 1)
            left_portion.reverse()
            right_portion = A[largest_idx + 1:]
            A = left_portion + right_portion

            # place largest element into it's respective position
            left_portion = A[:i + 1]
            answer.append(i + 1)
            left_portion.reverse()
            right_portion = A[i + 1:]
            A = left_portion + right_portion

        return answer

    def find_largest_element_idx(self, nums, end):
        '''
        find the index of the largest element in the num list
        :param nums: the num list
        :param end: the last index in the nums we're considering
        :return: the largest index
        '''
        largest_idx = end
        for i in reversed(range(0, end)):
            if nums[i] > nums[largest_idx]:
                largest_idx = i
        return largest_idx


if __name__ == "__main__":
    sol = Solution()

    result = sol.find_largest_element_idx([3, 2, 4, 1], 3)
    assert result == 2
    result = sol.find_largest_element_idx([3, 2], 1)
    assert result == 0
    result = sol.find_largest_element_idx([3], 0)
    assert result == 0

    result = sol.pancakeSort([3, 2, 4, 1])
    print(result)

    result = sol.pancakeSort([8, 10, 6, 4, 2, 9, 7, 5, 3, 1])
    print(result)
