				Project Ceasar Cipher

Hello and welcome!

This project is just a small project that runs code to generate a ceasar cipher.

A ceasar cipher is a very ancient way of hashing a message by taking one character in a string, and moving it over a given number of times in the alphabet:

For example, lets say we have a message we want to encode => message = "hello"

What this code does, is it takes each character in the variable message, and moves it over by one letter in the alphabet.

But lets say we have a message like this => message = "z"

The character "z" is the last letter in the alphabet, so how would the cipher hash this?

Well the answer is that this cipher, once reaching the end of the alphabet, starts a new at the beginning of the alphabet.

Ex ceaserCipher("z) => produces "z"





This project also comes with some unittests to check and make sure each function works exactly as is supposed to.  It tests these functions:

convertToNum => This is a function takes every character in a string message, and finds its index in the alphabet.  After each index is found, the message is returned except now as a list of indices in order equivalent to the message.

shiftNum => This function takes the previous list that was produced, and adds a shift to each index.  The result is list of numbers that reference a new position in the alphabet.

testNegativeShift => This function allows for a negative shift aka a left shift in the alphabet.  This is done by subtracting an index's positional value rather than adding.

testOutofBounds => There are two tests that check out of bounds, one checks to see if a letter is being shifted too much to the right such as with the character "z" being shifted to the right once, and one checks that a letter is not being shifted too far to the left, such as with the character "a" being shifted to the left.  In the functions file, however, it is just one function that produces a list with solutions for every character that did go out of bounds.  Ex "z" + shift to the right = "a", or "a" + shift to left = "z"


In the future, I would like to add an extension to this project that creates the mathematical solution to cracking the ceasar cipher using an average of appearance of characters in comparison to most common letters in alphabet.
