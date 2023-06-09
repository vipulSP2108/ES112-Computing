# Alien Language

After years of study, scientists at Google Labs have discovered an alien language transmitted from a faraway planet. The alien language is very unique in that every word consists of exactly L lowercase letters. Also, there are exactly D words in this language.

Once the dictionary of all the words in the alien language was built, the next breakthrough was to discover that the aliens have been transmitting messages to Earth for the past decade. Unfortunately, these signals are weakened due to the distance between our two planets and some of the words may be misinterpreted. In order to help them decipher these messages, the scientists have asked you to devise an algorithm that will determine the number of possible interpretations for a given pattern.

A pattern consists of exactly L tokens. Each token is either a single lowercase letter (the scientists are very sure that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ).

For example: (ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.

You are given two space-separated integers L and D as the first line of input. The next D lines contain one word each, and this comprises the set of all the words in the alien language. On the next and final line of input, you are given a single string which is a pattern P. Return the number of words in the alien language that match P.

# Example 

Input

>3 5
>
>abc 
>
>bca 
>
>dac 
>
>dbc 
>
>cba 
>
>(ab)(bc)(ca)

Output

>2

In the example above, the answer refers to the matches abc and bca.
