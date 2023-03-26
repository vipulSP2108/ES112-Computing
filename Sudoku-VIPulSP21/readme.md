# Sudoku

Sudoku is a popular single player game. The objective is to fill a 9x9 matrix with digits so that each column, each row, and all 9 non-overlapping 3x3 sub-matrices contain all of the digits from 1 through 9. Each 9x9 matrix is partially completed at the start of game play and typically has a unique solution.

Given a completed N^2xN^2 Sudoku matrix, your task is to determine whether it is a valid solution. A valid solution must satisfy the following criteria:

Each row contains each number from 1 to N^2, once each. Each column contains each number from 1 to N^2, once each. Divide the N^2 \times N^2 matrix into N^2 non-overlapping NxN sub-matrices. Each sub-matrix contains each number from 1 to N^2, once each. You don't need to worry about the uniqueness of the problem. Just check if the given matrix is a valid solution.

Input

The first line of the input is an integer N. The next N^2 lines describe a completed Sudoku solution, with each line contains exactly N^2 integers. All input integers are positive and less than 1000.

Output

Output "Yes" (quotes for clarity only) if it is a valid solution, or "No" (quotes for clarity only) if it is invalid.

# Example

Input

>3                      
>
>5 3 4 6 7 8 9 1 2       
>
>6 7 2 1 9 5 3 4 8
>
>1 9 8 3 4 2 5 6 7
>
>8 5 9 7 6 1 4 2 3
>
>4 2 6 8 5 3 7 9 1
>
>7 1 3 9 2 4 8 5 6>
>
>9 6 1 5 3 7 2 8 4
>
>2 8 7 4 1 9 6 3 5
>
>3 4 5 2 8 6 1 7 9

Output

>Yes

Input

>3
>
>1 2 3 4 5 6 7 8 9
>
>1 2 3 4 5 6 7 8 9
>
>1 2 3 4 5 6 7 8 9
>
>1 2 3 4 5 6 7 8 9
>
>1 2 3 4 5 6 7 8 9
>
>1 2 3 4 5 6 7 8 9
>
>1 2 3 4 5 6 7 8 9
>
>1 2 3 4 5 6 7 8 9
>
>1 2 3 4 5 6 7 8 9

Output

>No
