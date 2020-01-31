class Solution:

    def multiply(self, num1, num2):
        # reverse both strings since all math is done with LSD first
        product = self._multiply(num1[::-1], num2[::-1])
        # reverse to give back string answer in normal form
        return product[::-1]

    def _multiply(self, num1, num2):
        '''
        Returns numbers in reverse order
        :param num1: reverse order of num
        :param num2: reverse order of num
        :return: reverse order of product
        '''
        answer = ""
        for num1_i in range(len(num1)):
            result = ""
            carry = 0
            for num2_i in range(len(num2)):
                m_1 = int(num1[num1_i])
                m_2 = int(num2[num2_i])
                product = m_1 * m_2
                product += carry
                digit = product % 10
                carry = int(product / 10)
                result += str(digit)

            # add carry if there is one
            if carry != 0:
                result += str(carry)

            # add power of 10
            for power in range(num1_i):
                result = "0" + result

            answer = self.add_nums(answer, result)
        return answer

    def add_nums(self, str_num1, str_num2):
        '''
        Returns numbers in reverse order
        :param str_num1: reverse order of num
        :param str_num2: reverse order of num
        :return: reverse order of sum
        '''
        i = 0
        carry = 0
        result = ""
        zero_sum = 0
        while i < len(str_num1) and i < len(str_num2):
            temp_sum = int(str_num1[i]) + int(str_num2[i])
            temp_sum += carry
            digit = temp_sum % 10
            carry = int(temp_sum / 10)
            result += str(digit)
            zero_sum += digit
            i += 1

        while i < len(str_num1):
            temp_sum = int(str_num1[i])
            temp_sum += carry
            digit = temp_sum % 10
            carry = int(temp_sum / 10)
            result += str(digit)
            zero_sum += digit
            i += 1

        while i < len(str_num2):
            temp_sum = int(str_num2[i])
            temp_sum += carry
            digit = temp_sum % 10
            carry = int(temp_sum / 10)
            result += str(digit)
            zero_sum += digit
            i += 1

        if carry != 0:
            result += str(carry)

        # handle repetitive zeros
        if zero_sum == 0:
            return "0"
        return result


if __name__ == "__main__":
    sol = Solution()

    # 34 + 22 = 56
    result = sol.add_nums("22", "43")
    assert result == "65"

    result = sol.add_nums("00", "00")
    assert result == "0"

    # 34 + 22 = 56
    result = sol.add_nums("22", "34")
    assert result == "56"

    result = sol.multiply("9133", "0")
    assert result == "0"

    result = sol.multiply("9", "9")
    assert result == "81"

    result = sol.multiply("98", "9")
    assert result == "882"

    result = sol.multiply("11", "1")
    assert result == "11"

    result = sol.multiply("11", "11")
    assert result == "121"

    result = sol.multiply("11", "10")
    assert result == "110"

    result = sol.multiply("9", "98")
    assert result == "882"

    result = sol.multiply("99", "98")
    assert result == "9702"

    result = sol.multiply("2", "3")
    assert result == "6"

    result = sol.multiply("123", "456")
    assert result == "56088"

    result = sol.multiply("123456789", "123456")
    assert result == "15241481342784"

    result = sol.multiply("0", "0")
    assert result == "0"

    result = sol.multiply("1", "0")
    assert result == "0"
