# Discrete Mathematics Coding Assignment 1

## Overview
This Python program includes various functions for character and string manipulation, as well as two different implementations of the Fibonacci sequence calculator. The assignment covers vowel counting, secret code decoding, and comparing recursive vs iterative approaches to computing Fibonacci numbers.

## Author
- **Name:** Thuy Vy Tran
- **UNI:** tt2964

## Features

### Part A: Vowel Counting and String Manipulation
1. **vowel_counter(s)**: Counts the number of vowels (a, e, i, o, u) in a lowercase string.
2. **sometimes_y(s)**: Implements the "sometimes y" rule where 'y' at the end of a word counts as a vowel. Returns:
   - Whether 'y' is in the string (boolean)
   - Number of vowels without the 'y' rule
   - Number of vowels with the 'y' rule applied
3. **sentence_counter(sentence)**: Splits a sentence into words and counts vowels in each word, returning a list of vowel counts.

### Secret Code Functions
4. **create_code(secret_alphabet)**: Creates a decoder dictionary that maps characters from a secret alphabet to the standard English alphabet.
5. **decode(decoder, encoded_word)**: Decodes a word using the decoder dictionary.

### Part B: Fibonacci Implementations
6. **recursive_fib(n)**: Calculates the nth Fibonacci number using recursion with memoization.
7. **iterative_fib(n)**: Calculates the nth Fibonacci number using iteration.

## Usage
Run the script to execute all test cases for each function. The program will display whether each test passes or fails, showing:
- The expected output
- Your function's actual output
- A PASSED/FAILED status for each test

```
python coms3203_assignment1.py
```

## Test Cases
The program includes comprehensive test cases for each function:
- Vowel counting with different words
- "Sometimes y" rule applied to various scenarios
- Sentence parsing and vowel counting
- Secret code creation and decoding
- Fibonacci sequence calculation (both recursive and iterative)

## Implementation Notes
- The recursive Fibonacci function uses memoization to improve performance
- String manipulation functions handle punctuation and capitalization appropriately
- All functions include proper docstrings explaining parameters and return values