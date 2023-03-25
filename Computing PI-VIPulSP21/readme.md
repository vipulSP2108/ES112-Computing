# Instructions

The mathematical constant π is given by the generalized continued fraction 3 + 1²/(6 + 3²/(6 + 5²/(6 + 7²/...))) (See the first one in image). Given a a non-negative integer as input. Compute π up to that depth in the continued fraction given.

On input:

>0

we get:

>3

On input:

>1

we get:

>19/6

which is obtained by evaluating upto the first level of the continued fraction. i.e., 3+1/6.

On input:

>5

we get:

>21779/6930

which is 3+1/(6+9/(6+25/(6+36/(6+49/(6+81/6))))).

# IMPORTANT: 
Using float to store your values will not work. See Python's fractions.
