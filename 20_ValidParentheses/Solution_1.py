expected_chars = {
    '(' : ')',
    '{' : '}',
    '[' : ']'
}

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Use a stack to keep track of what type is opened.
        # We can only close when the top of the stack has the opening brace

        # Open add to stack
        # Close remove from stack if brace matches, otherwise false

        parentheses_stack = []

        for char in s:
            # add to stack if there is an open paren
            if char in expected_chars:
                parentheses_stack.append(char)
            # pop from stack if we can pop and there is a closing brace
            elif (len(parentheses_stack) > 0) and (char in expected_chars.values()):
                last_char = parentheses_stack.pop()
                # check if the current character is the expected char
                if expected_chars[last_char] is not char:
                    return False
            else:
                return False

        # if the stack is not empty then we have a dangling paren
        if len(parentheses_stack) is not 0:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()

    # result = sol.isValid("()")
    # assert result == True
    #
    # result = sol.isValid("()[]{}")
    # assert result == True
    #
    # result = sol.isValid("(]")
    # assert result == False
    #
    # result = sol.isValid("([)]")
    # assert result == False
    #
    # result = sol.isValid("{[]}")
    # assert result == True
    #
    # result = sol.isValid("[")
    # assert result == False

    result = sol.isValid("]")
    assert result == False

    result = sol.isValid("")
    assert result == True