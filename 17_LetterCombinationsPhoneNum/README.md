# LetterCombinationsPhoneNum

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letter

### Runtime and Space Complexity
The solution is recursive.
The runtime is subject the number of digit and the number of iterations that are possible with the list of numbers each digit produces.

The numbers with the largest list are 7 and 9 with a list of 4 each
The numbers with the second largest list is everything else with 3 each
The respective size of `combinations` will grow by the number of possible digits that need to be held.
The respective since the `combinations` need to be found, it will grow at the same size

- "2" -> O(3^1)
-"22" -> O(3^2)
- "222" -> O(3^3)
- "7" -> O(4^1)
- "77" -> O(4^2)
- "777" -> O(4^3)
- "27" -> O(3^1 * 4^1)
- "2277" -> O(3^2 * 4^2)

Runtime: O(3^n * 4^n)

Space: O(3^n * 4^n)
