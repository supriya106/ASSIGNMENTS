Our value can be a string, number, or object
We need to return a boolean value
A palindrome ignores case, spaces, and punctuation

Pseudocode
First, we need to consider the type of value.

If it is a number, we need to change it to a string to compare how it reads backwards and forwards.
If it is an object, we need to somehow also change it to a string to do a comparison.
If it is a string, we can forge ahead.
If we have null or undefined, how do we handle that?

We also need to take care to ignore whether or not letters or uppercase or lowercase.
We can do that by either making everything capitalized or everything lowercase.