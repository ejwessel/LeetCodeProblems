from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_pos = len(nums1) - 1
        m_pos = m - 1
        n_pos = n - 1
        while m_pos >= 0 and n_pos >= 0:
            if nums1[m_pos] >= nums2[n_pos]:
                nums1[insert_pos] = nums1[m_pos]
                m_pos -= 1
                insert_pos -= 1
            else:
                nums1[insert_pos] = nums2[n_pos]
                n_pos -= 1
                insert_pos -= 1

        while n_pos >= 0:
            nums1[insert_pos] = nums2[n_pos]
            n_pos -= 1
            insert_pos -= 1


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    # test all numbers in nums1 > nums2
    nums1 = [7, 8, 9, 0, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 5, 6]
    n = 4
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 5, 6, 7, 8, 9]

    # test all numbers in nums2 > nums2
    nums1 = [1, 3, 5, 0, 0, 0, 0]
    m = 3
    nums2 = [7, 8, 9, 10]
    n = 4
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1, 3, 5, 7, 8, 9, 10]

    # test interwoven
    nums1 = [1, 3, 5, 7, 0, 0, 0, 0]
    m = 4
    nums2 = [2, 4, 8, 10]
    n = 4
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4, 5, 7, 8, 10]
