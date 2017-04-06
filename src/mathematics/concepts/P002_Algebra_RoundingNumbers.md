# Description: Rounding Numbers

## Concepts
### Rounding Up
- Rounding up a number x means getting the smallest integer not less than x.
- It is equivalent to rounding towards positive infinity.
- Examples
    - Rounding up 1.2 will yield 2.
    - Rounding up 1.9 will yield 2.
    - Rounding up -1.2 will yield -1.
    - Rounding up 341 to the nearest hundred will yield 400.
    - Rounding up 350 to the nearest hundred will yield 400.

### Rounding Down
* Rounding down a number x means getting the largest integer not greater than x.
* It is equivalent to rounding towards negative infinity.
* Examples
    - Rounding down 1.9 will yield 1.
    - Rounding down -1.9 will yield -2.
    - Rounding down 341 to the nearest hundred will yield 300.
    - Rounding down 350 to the nearest hundred will yield 300.

### Truncating
* Truncating a number x means getting a number with the fractional portion removed.
* It is equivalent to rounding towards zero.
* Examples
    - Truncating 1.23 will yield 1.
    - Truncating 1.51 will yield 1.
    - Truncating -1.99 will yield -1.

### Rounding
* The rounding of a number x means getting the number nearest to x.
* Rounding Rules
    - If the number to be rounded is followed by 5, 6, 7, 8, or 9, the number is rounded up. 
    - Example: 48 rounded to the nearest ten is 40.
    - If the number to be rounded is followed by 0, 1, 2, 3, or 4, the number is rounded down.
    - Example: 43 rounded to the nearest ten is 40.
* Examples
    - Rounding 1.23 will yield 1.
    - Rounding 1.50 will yield 2.
    - Rounding 1.51 will yield 2.
    - Rounding -1.21 will yield 
    - Rounding 341 to the nearest hundred will yield 300.
    - Rounding 350 to the nearest hundred will yield 400.

## Number Charts
* None

## Code
* Octave Code: [Rounding Numbers](../../code/octave/P001_Algebra_RoundingNumbers.m)
* Python Code: [Rounding Numbers](../../code/python/P001_Algebra_RoundingNumbers.py)
* R Code: [Rounding Numbers](../../code/r/P001_Algebra_RoundingNumbers.R)

## TODO
* Program to round up a number (Say 341) to the nearest hundred (should give 400).
