from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 0 or len(cost) == 0:
            return -1
        if sum(gas) < sum(cost):
            return -1

        b = 0
        e = 0
        amount = (gas[b] - cost[b])
        if amount >= 0:
            e += 1
            e %= len(gas)
            amount += gas[e] - cost[e]
        else:
            b -= 1
            if b < 0:
                b = len(gas) - 1
            amount += gas[b] - cost[b]

        while b != e:
            if amount >= 0:
                e += 1
                e %= len(gas)
                amount += gas[e] - cost[e]
            else:
                b -= 1
                if b < 0:
                    b = len(gas) - 1
                amount += gas[b] - cost[b]

        if amount >= 0:
            return b
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    result = sol.canCompleteCircuit(gas, cost)
    assert result == 3

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    result = sol.canCompleteCircuit(gas, cost)
    assert result == -1

    gas = []
    cost = []
    result = sol.canCompleteCircuit(gas, cost)
    assert result == -1

    gas = [5]
    cost = [5]
    result = sol.canCompleteCircuit(gas, cost)
    assert result == 0

    # this problem does not have a unique solution
    gas = [5, 6, 7, 4, 3, 6, 2, 1, 9, 6]
    cost = [6, 5, 4, 10, 8, 7, 1, 1, 1, 3]
    result = sol.canCompleteCircuit(gas, cost)
    assert result == 8

    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]
    result = sol.canCompleteCircuit(gas, cost)
    assert result == 4
