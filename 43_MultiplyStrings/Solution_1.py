class Solution:

    def multiply(self, num1, num2):
        return self._multiply(num1, num2, len(num1))

    def _multiply(self, num1, num2, power_of_ten):
        if len(num1) == 1:
            carry = 0
            string_result = ""
            for num in num2:
                temp_product = int(num1) * int(num)
                temp_product += carry
                digit = temp_product % 10
                carry = int(temp_product / 10)
                string_result += str(digit)

            if carry != 0:
                string_result = str(carry) + string_result

            for i in range(power_of_ten):
                string_result += "0"
            return string_result
        elif len(num1) > 1:
            summed_val = ""
            for i in range(len(num1)):
                value_to_add = self._multiply(num1[i], num2, len(num1) - 1 - i)
                summed_val = self.add_nums(value_to_add, summed_val)
            return summed_val

    def add_nums(self, str_num1, str_num2):
        lsd_str_num1 = str_num1[::-1]
        lsd_str_num2 = str_num2[::-1]
        i = 0
        carry = 0
        result = ""
        while i < len(lsd_str_num1) and i < len(lsd_str_num2):
            temp_sum = int(lsd_str_num1[i]) + int(lsd_str_num2[i])
            temp_sum += carry
            digit = temp_sum % 10
            carry = int(temp_sum / 10)
            result += str(digit)
            i += 1

        while i < len(lsd_str_num1):
            temp_sum = int(lsd_str_num1[i])
            temp_sum += carry
            digit = temp_sum % 10
            carry = int(temp_sum / 10)
            result += str(digit)
            i += 1

        while i < len(lsd_str_num2):
            temp_sum = int(lsd_str_num2[i])
            temp_sum += carry
            digit = temp_sum % 10
            carry = int(temp_sum / 10)
            result += str(digit)
            i += 1

        if carry != 0:
            result += str(carry)
        return result[::-1]


if __name__ == "__main__":
    sol = Solution()

    result = sol.add_nums("98", "7")
    assert result == "105"

    result = sol.add_nums("7", "98")
    assert result == "105"

    result = sol.add_nums("0", "0")
    assert result == "0"

    result = sol.add_nums("0", "98")
    assert result == "98"

    # result = sol.multiply("98", "9")
    # assert result == "882"
    #
    # result = sol.multiply("11", "1")
    # assert result == "11"
    #
    # result = sol.multiply("11", "11")
    # assert result == "121"
    #
    # result = sol.multiply("11", "10")
    # assert result == "110"

    result = sol.multiply("99", "98")
    print(result)
    assert result == "9702"

    # result = sol.multiply("9", "98")
    # print(result)
    # assert result == "882"
    #
    # result = sol.multiply("2", "3")
    # assert result == "6"

    # result = sol.multiply("123", "456")
    # assert result == "56088"

