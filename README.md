# multiple-bases-compression-algorithm
An algorithm I invented one night to combine and compress information with multiple bases.

## Problem
Let's say you have 3 pieces of unrelated information. The first piece can be in one of 3 states. The other two have 4 and 5 states, respectively. A naive approach would store this information in 7 bits (2+2+3). However, the optimal number of bits to store this information is 6: `ceil(log_2(3*4*5))=6`. This algorithm can store suh information optimally.

## Simple case
Let's store 3 pieces of information, each with 10 possible states, in the minimum 10 bits. We can represent each piece of information as one base-10 digit. Therefore we'll end up with a 3-digit base-10 number, with a maximum value of 999, and 100 possible states total. This can be converted to binary to be stored in 10 bits.

## General case
// TODO: write

## Use cases
