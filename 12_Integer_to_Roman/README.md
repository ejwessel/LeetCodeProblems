# Solution 1
This solution evaluates from Most Signigicant Digit(MSD) to Least Significant Digit (LSD)
## Runtime Analysis
O(max(len(num), num/1000) which is more or less O(n)

If the number is < 2000, all digits will be looked at exactly once.

If the number is >= 2000, the 1000 denomination need to be duplicated (int)number/1000 number of times.

Since M is the largest allowed denomination we need to construct the total number of Ms needed to represent that denomination.

i.e. 1999 -> MCMXCIX

i.e. 9999 -> MMMMMMMMMCMXCIX

getLeftdigit() and getNumDigits() add to the complexity of this and slow it down. This is because the number being evaluated  goes from a number representation to a string back to a number representation. This is done for every evaluation of a number.

## Space Analysis
O(n)
The total number of actual roman numerals is bounded by the total number of elements in general. 

After 2000, the total number of characters is dominated by how many thousands are in the number and grows linearly to this num/1000

### Bug:
Solution 1 doesn't handle numbers >= 2000 properly

i.e. 20999 fails because 0999 is evaluated as a number. This breaks the code.

# Solution 2
Evaluates from LSD to MSD

## Runtime Analysis
O(n^2)
I thought I was being clever with identifying the number of 10s and right right most digit.
However, this is O(n^2) becuase I subtract from the provided number starting with the LSD, but the number of places of the number that are evaluated in getLeftDigit() and getNumTens() remain constant. This results in all number places being evaluted n times

## Space Analysis
O(n)
Same as Solution 1

# Solution 3
This is the cleanest and most optimized verison.

This evaluates from LSD to MSD

## Runtime Analysis
O(max(len(num), num/1000) which is more or less O(n)

I cache the position of the 10's place using tens_place so I don't need to find the left most digit starting from the LSD


## Space Analysis
O(n)
Same as Solution 1

