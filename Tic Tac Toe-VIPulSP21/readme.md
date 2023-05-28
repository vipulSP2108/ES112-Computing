# Instructions

The input is a completed, full position on a tic-tac-toe board. Determine who won, x or o or a draw. The input is in two lines, the first line is five positions of x, the second line is 4 positions of “o”. The positions for each player will be given in increasing order.

Board positions:

First row is 0, 1, 2,

second row is 3, 4, 5,

third row is 6, 7, 8.

Both players can’t win.

Example,

0 1 4 5 8

2 3 6 7

This means:

x|x|o 
o|x|x
o|o|x

Answer: x

Example:

0 1 5 6 8
2 3 4 7 
This means:
x|x|o 
o|o|x
x|o|x 
Answer: draw

Input

First line contains input by player one and second line contains input by player 2.

Output

x or o or draw

Input 1

>0 1 4 5 8
>
>2 3 6 7

Output 1

>x

Input 2

>0 1 5 6 8
>
>2 3 4 7

Output 2

> draw
