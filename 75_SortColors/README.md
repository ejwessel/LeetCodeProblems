## Sort Colors

- I wasn't able to figure this problem out. 
- I understood that there were only two possibilities for numbers to go since the only values were 0, 1, 2;
This means left, middle, right
- I tried to prepend or append the numbers to the ends, but that results in O(n) removal
- I got stuck at this part and it should have been apparent that I should have used two pointers.
One for the beginning and one for the end

Runtime: O(n)
- every element is looked at once

Space: O(1)
- rearranging is done in place