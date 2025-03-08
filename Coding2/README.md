# Discrete Mathematics Coding Assignment 2: Propositional Logic

## Overview
This Python program implements a propositional logic evaluator that can format and evaluate nested logical propositions. The assignment focuses on handling different logical operators including NOT, AND, OR, IF (implies), IFF (if and only if), and XOR.

## Features

### 1. Proposition Formatting (`format_prop` function)
Converts a proposition in nested list form to a readable string format:
- Handles atomic propositions (e.g., "p1", "p2")
- Implements unary operator: NOT
- Implements binary operators: AND, OR, IF (->), IFF (<->), XOR
- Returns properly formatted proposition strings with appropriate parentheses

### 2. Proposition Evaluation (`eval_prop` function)
Evaluates a proposition given truth values for each atomic variable:
- Returns 1 for True and 0 for False
- Recursively evaluates nested propositions
- Correctly implements the truth tables for all logical operators
- Handles complex nested propositions with multiple operators

## Examples

The program includes several test cases demonstrating how to:
1. Evaluate simple NOT proposition
2. Evaluate AND proposition
3. Evaluate IFF (if and only if) proposition
4. Evaluate a complex nested proposition: `(p1 AND (NOT p2)) -> p3`
5. Evaluate another complex proposition: `p1 <-> (p2 OR (NOT p3))`

## Usage

To run the program:
```
python coding2.py
```

The output will show:
- The formatted proposition in readable form
- The truth values assigned to each atomic variable
- The evaluation result (0 or 1)

## Implementation Details

The program uses a recursive approach to handle nested propositions:
- Base case: Single atomic proposition (e.g., "p1")
- Unary operator case: NOT operation on a proposition
- Binary operator case: Operations between two propositions (AND, OR, IF, IFF, XOR)

Each logical operation is implemented according to its truth table:
- AND: Returns 1 only if both operands are 1
- OR: Returns 1 if either operand is 1
- IF (implies): Returns 0 only when the antecedent is 1 and the consequent is 0
- IFF (if and only if): Returns 1 when both operands have the same value
- XOR: Returns 1 when the operands have different values

## Requirements
- Python 3
- The `itertools` module (included in standard Python)