# Instructions

Given a tuple ip of n entries in the function yourCodeHere, create and return another tuple containing same numbers as in original tuple except that all -1 are replaced with the floor of average of the neighbour. Assume that all -1 is surrounded with non-negative numbers.

Input

First line containes the total numbers of entries that would be entered (n).
Next n consecutive line containes each entry
Output

Entries with all -1 replaced with the floor of average of neighbours.

NOTE:

Don't remove the existing code
No need to write code for taking input and printing output
Write your code in the function yourCodeHere only
The tuple of entries in input is in the variable ip
You must return the resultant tuple otherwise the code will raise error

# Example

Input:

>6
>
>1
>
>2
>
>-1
>
>2
>
>-1
>
>5

Output:

>(1 2 2 2 3 5)
