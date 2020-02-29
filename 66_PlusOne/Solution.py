from typing import List
from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        answer = deque()
        for i in reversed(range(len(digits))):
            if i == len(digits) - 1:
                sum = digits[i] + 1
            else:
                sum = digits[i] + carry
            val = sum % 10
            carry = sum // 10
            answer.appendleft(val)
        if carry is not 0:
            answer.appendleft(carry)
        return list(answer)

if __name__ == "__main__":
    sol = Solution()
    result = sol.plusOne([1, 2, 3])
    assert result == [1, 2, 4]

    result = sol.plusOne([1, 9, 9])
    assert result == [2, 0, 0]

    result = sol.plusOne([9, 9, 9])
    assert result == [1, 0, 0, 0]

    result = sol.plusOne([0])
    assert result == [1]
