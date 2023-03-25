# Instructions

We'll write a quadratic solver that prints out solutions in a nice form.

Your program should take as input integers a, b, and c in the quadratic equation ax² + bx + c = 0 and print its roots in a nice format.

If the discriminant is a perfect square, then it should print out both solutions as rational numbers like so:

On input:

>1 8 15

we get:

>(-3, -5)

If the discriminant is not a perfect square but positive, then it should print it like so:

On input:

>1 3 1

The output should be:

>(-3 ± √5)/2

If the discriminant is negative, then you should print it out like so:

On input:

>1 1 1

we should get:

>(-1 ± i√3)/2

Do not use Python's float. See https://docs.python.org/3/library/fractions.html.
