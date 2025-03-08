# Discrete Mathematics Coding Assignment 4: Number Theory

## Overview
This Python program implements fundamental number theory algorithms including Euclid's algorithm for finding the greatest common divisor (GCD), prime number generation using the Sieve of Eratosthenes, and verification of Goldbach's Conjecture for even numbers.

## Features

### Part A: Euclid's Algorithm
The program implements Euclid's algorithm to find the greatest common divisor (GCD) of two integers.

- **Function**: `euclid(num1, num2)`
- **Approach**: Uses the recursive property that gcd(a,b) = gcd(b, a mod b)
- **Output**: Returns the GCD and prints the intermediate steps of the algorithm
- **Example**: 
  ```
  GCD(252,105) = GCD(105,42) = GCD(42,21) = GCD(21,0) = 21
  ```

### Part B: Prime Number Generation
Implements a prime number generator that returns all prime numbers up to a given integer n.

- **Function**: `prime_gen(n)`
- **Approach**: Uses a modified Sieve of Eratosthenes algorithm
- **Output**: Returns a list of all prime numbers less than or equal to n
- **Example**:
  ```
  prime_gen(42) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
  ```

### Part C: Goldbach's Conjecture
Verifies Goldbach's Conjecture, which states that every even integer greater than 2 can be expressed as the sum of two primes.

- **Function**: `check_goldbach(n)`
- **Approach**: Generates prime numbers up to n and checks pairs to find two that sum to n
- **Output**: Returns a list of two prime numbers that sum to n
- **Example**:
  ```
  check_goldbach(8) = [3, 5]
  ```

## Usage
Run the script to execute test cases for each function:

```
python coding4.py
```

The program will display:
- The calculated GCD with intermediate steps
- Generated prime numbers up to the specified limit
- Two prime numbers that sum to the given even number (Goldbach's Conjecture)

## Test Cases
The program includes multiple test cases:

1. **Euclid's Algorithm**:
   - GCD of 252 and 105
   - GCD of 1071 and 462
   - GCD of 85523 and 3212

2. **Prime Number Generation**:
   - Primes up to 42
   - Primes up to 314
   - Primes up to 884

3. **Goldbach's Conjecture**:
   - Finding two primes that sum to 8
   - Finding two primes that sum to 482
   - Finding two primes that sum to 1152

## Implementation Notes
- The prime generation algorithm could be optimized further for larger numbers
- Goldbach's Conjecture implementation may return different valid prime pairs than the expected answers, as long as they sum to the target number