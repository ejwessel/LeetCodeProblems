from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = self._restore(s, 3)
        return result

    def _restore(self, s, k):
        # edge case
        if len(s) == 0:
            return []

        # no more depth
        if k == 0:
            # condition catches straggler 0s in beginning
            if len(s) != len(str(int(s))):
                return []
            # checks if in range
            elif not 0 <= int(s) <= 255:
                return []
            else:
                return [s]
        else:
            result = []
            for i in range(1, 4):
                b = s[:i]

                # validates level before going down
                if len(b) != len(str(int(b))):
                    continue
                # checks value is within allowed range
                elif not 0 <= int(b) <= 255:
                    continue
                # recurse downward and handles result
                else:
                    list = self._restore(s[i:], k - 1)
                    for item in list:
                        result.append(b + '.' + item)
            return result


if __name__ == "__main__":
    sol = Solution()

    result = sol.restoreIpAddresses('25525511135')
    assert result == ['255.255.11.135', '255.255.111.35']

    result = sol.restoreIpAddresses('010010')
    assert result == ['0.10.0.10', '0.100.1.0']

    result = sol.restoreIpAddresses('1111')
    assert result == ['1.1.1.1']

    result = sol.restoreIpAddresses('11111')
    assert result == ['1.1.1.11', '1.1.11.1', '1.11.1.1', '11.1.1.1']

    result = sol.restoreIpAddresses('111')
    assert result == []

