class Solution:
    def simplifyPath(self, path: str) -> str:
        # break into components and get rid of empty string in the beginning
        components = path.split('/')[1:]
        path_stack = []

        for component in components:
            if component == '':
                continue
            elif component == '.':
                continue
            elif component == '..':
                # can only pop if there are elements, otherwise ignore
                if len(path_stack) == 0:
                    continue
                path_stack.pop()
            else:
                path_stack.append(component)

        return '/' + '/'.join(path_stack)

if __name__ == "__main__":
    sol = Solution()

    input = '/a//b/c/cd/.././'
    result = sol.simplifyPath(input)
    assert result == '/a/b/c'

    input = '/home/'
    result = sol.simplifyPath(input)
    assert result == '/home'

    input = '/../'
    result = sol.simplifyPath(input)
    assert result == '/'

    input = '/home//foo/'
    result = sol.simplifyPath(input)
    assert result == '/home/foo'

    input = '/a/./b/../../c/'
    result = sol.simplifyPath(input)
    assert result == '/c'

    input = '/a/../../b/../c//.//'
    result = sol.simplifyPath(input)
    assert result == '/c'

    input = '/a//b////c/d//././/..'
    result = sol.simplifyPath(input)
    assert result == '/a/b/c'

    input = '/a//b///c/d//././/..'
    result = sol.simplifyPath(input)
    assert result == '/a/b/c'

    input = '/../..'
    result = sol.simplifyPath(input)
    assert result == '/'

    input = '/'
    result = sol.simplifyPath(input)
    assert result == '/'

    input = '/./././././././'
    result = sol.simplifyPath(input)
    assert result == '/'

    input = '/////////'
    result = sol.simplifyPath(input)
    assert result == '/'



