# Instructions

Given a list of numbers, find two numbers whose sum is equal to the target number. And a number should be considered only once from the list.

Input:

First line contains number of elements list will contain.
Second line contains the list of numbers.
Third line contains the target number.
Note: As in the second line input list will be in the form of string, therefore to convert this string into list of numbers you can use below code

lst = list(map(int, lst_str.split()))
Here, lst is the final list of numbers and "lst_str" is the input list which will be in the form of string.

Output:

Print YES if two numbers exist whose sum is equal to the target number else print NO.

Input 1:

>7
>
>2 3 4 11 6 1 9
>
>10

Output 1:

>YES

Input 2:

>8
>
>4 7 3 9 16 6 24 0
>
>5

Output 2:

>NO
