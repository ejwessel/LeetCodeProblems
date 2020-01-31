I remove a lot of the needless complexity with regex

Note: `match()` seraches from the beginning of the string

## Runtime Analysis:
All my operations are string operations that use the re module to some extent. It's likely what causes the most expensive operations with regards to time
searching worst case is O(n) time if we match against more or less the entire input string
stripping worst case is O(n) time if there is more or less all whitespace
Overall worst case complexity is O(n)

## Space Analysis:
intermediate objects are the input_match and matched_string
input_match is an object that contains the matched string which I strip and then save into another variable matched_string.
space worst case is roughly O(2n) => O(n)
