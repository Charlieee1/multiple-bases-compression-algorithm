# multiple-bases-compression-algorithm
An algorithm I invented one night to combine and compress information with multiple bases. I do not know if this has been discovered before. The closest algorithm I can find is the [Double Dabble algorithm](https://en.wikipedia.org/wiki/Double_dabble).

## Problem
Let's say you have 3 pieces of unrelated information. The first piece can be in one of 3 states. The other two have 4 and 5 states, respectively. A naive approach would store this information in 7 bits (2+2+3). However, the optimal number of bits to store this information is 6: `ceil(log_2(3*4*5))=6`. This algorithm can store such information optimally.

## Simple case
Let's store 3 pieces of information, each with 10 possible states, in the minimum 10 bits. The naive approach would use 12 bits. We can represent each piece of information as one base-10 digit. Therefore we'll end up with a 3-digit base-10 number, with a maximum value of 999, and 100 possible states total. This can be converted to binary to be stored in 10 bits.

## General case
We will now store 3 pieces of information, 3, 4, and 5 states respectively, as in the introduction. The naive approach uses 7 bits. We start with a number 0 that is our encoded information. We add to it the first piece of information (3 possible states, from 0 to 2). Next, we multiply the second piece of information (0 to 3) by the amount of possible states in the first piece (3). We add the product to the encoded number. For the final piece of information, we multiply it (0 to 4) by the amounts of possible states in the first two pieces (3*4), and add it to the encoded number. The encoded number will have a minimum value of 0, and a maximum value of `2+3*3+4*4*3=59`. Taking log base 2 of 60 (possible states) and rounding up, the encoded number requires 6 bits to store.  
This can be expanded to use more pieces of information, and different amounts of states for each piece.

## Decoding
// TODO: write

## Implementation

## Use cases
