# Discrete Mathematics Coding Assignment 3: Functions and Relations

## Overview
This Python program implements functions to determine various properties of mathematical functions and relations. The assignment is divided into two main parts: function properties and relation properties.

## Author
- **Name:** Thuy Vy Tran
- **UNI:** tt2964

## Features

### Part A: Function Properties
Functions that determine whether a given function (represented as a mapping) has certain mathematical properties:

1. **is_onto(domain, co_domain, mapping)**: 
   - Checks if a function is onto (surjective)
   - A function is onto if every element in the co-domain has at least one corresponding element in the domain

2. **is_one_to_one(domain, co_domain, mapping)**:
   - Checks if a function is one-to-one (injective)
   - A function is one-to-one if each element in the co-domain corresponds to at most one element in the domain

3. **is_bijective(domain, co_domain, mapping)**:
   - Determines if a function is bijective
   - A function is bijective if it is both onto and one-to-one

### Part B: Relation Properties
Functions that determine whether a given relation (represented as an adjacency matrix) has certain mathematical properties:

1. **is_reflexive(adj_mat)**:
   - Checks if a relation is reflexive
   - A relation is reflexive if (a,a) is in the relation for all elements a

2. **is_symmetric(adj_mat)**:
   - Checks if a relation is symmetric
   - A relation is symmetric if (a,b) in the relation implies (b,a) is also in the relation

3. **is_transitive(adj_mat)**:
   - Checks if a relation is transitive
   - A relation is transitive if (a,b) and (b,c) in the relation implies (a,c) is also in the relation

4. **is_antisymmetric(adj_mat)**:
   - Checks if a relation is antisymmetric
   - A relation is antisymmetric if (a,b) and (b,a) in the relation implies a = b

5. **is_irreflexive(adj_mat)**:
   - Checks if a relation is irreflexive
   - A relation is irreflexive if (a,a) is not in the relation for all elements a

### Helper Functions
1. **mapToSet(adj_map)**:
   - Converts an adjacency matrix to a set of ordered pairs representing the relation

2. **find(l, first, second)**:
   - Utility function to find if an ordered pair exists in a list of ordered pairs

## Usage
Run the script to execute test cases for each function:

```
python coding3.py
```

The program will display PASSED/FAILED status for each test, comparing your implementation's results with the expected answers.

## Implementation Notes
- Functions are represented as dictionaries mapping domain elements to co-domain elements
- Relations are represented as adjacency matrices where adj_mat[i][j] = 1 if the relation holds between i+1 and j+1
- The code includes comprehensive test cases for each property