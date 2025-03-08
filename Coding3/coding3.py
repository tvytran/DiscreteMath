#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 3
#
# Before submitting the file to gradescope make sure of the following:
# 1. The name of the file is coding3.py
# 2. Nothing below the line `if __name__="__main__":` is changed
# 3. Make sure there are no indentation errors and that the code compiles on your end
#
# YOUR NAME: Thuy Vy Tran
# YOUR UNI: tt2964
def mapToSet(adj_map):
    this_list = []
    r = 0
    while(r < len(adj_map)):
        c = 0
        while(c < len(adj_map[0])):
            if(adj_map[r][c] == 1):
                this_list.append((r+1,c+1))
            c+=1 
        r += 1
    return this_list
                
    
def is_onto (domain, co_domain, mapping):
    """Determines if the function is onto.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in the co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]
    """
    if(len(mapping) < len(co_domain)):
        return False
    ran = []
    for key in mapping:
        ran.append(mapping[key])
    for element in ran:
        i = 0
        while(i < len(co_domain)):
            if(co_domain[i] == element):
                co_domain.remove(element)
            i += 1
    
    if(len(co_domain) > 0):
        return False
    return True
                
    


def is_one_to_one (domain, co_domain, mapping):
    """Determines if the function is one-to-one.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in teh co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]

    """
    ran = []
    for key in mapping:
        ran.append(mapping[key])
    
    index = 0
    for element in ran:
        i = 0
        while(i < len(ran)):
            if(index != i and ran[i] == element):
                return False
            i += 1
        index += 1
    return True

def is_bijective ( domain , co_domain , mapping ) :
    """Determines if the function is bijective.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in teh co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]

    """
    if(is_one_to_one(domain,co_domain,mapping) and is_onto(domain,co_domain,mapping)):
        return True
    return False

def is_reflexive (adj_mat) :
    """Determines if the relation is reflexive.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    if(len(adj_mat) != len(adj_mat[0])):
        return False
    i = 0
    while(i < len(adj_mat)):
        if(adj_mat[i][i] != 1):
            return False
        i += 1
    return True

def is_symmetric (adj_mat) :
    """Determines if the relation is symmetric.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    listed = mapToSet(adj_mat)
    i = 0
    while i < len(listed):
        first = listed[i][0]
        second = listed[i][1]
        if(first == second):
            i += 1
        else:
            j = 0
            count = 0
            while j < len(listed):
                f2 = listed[j][0]
                s2 = listed[j][1]
                if(first == s2 and second == f2):
                    count += 1
                    break
                j += 1
            if(count == 0):
                return False
        i += 1
        
    return True            
def find(l, first, second):
    i = 0
    while(i < len(l)):
        if(l[i][0] == first and l[i][1] == second):
            return True
        i += 1
    return False
def is_transitive (adj_mat) :
    """Determines if the relation is transitive.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    listed = mapToSet(adj_mat)
    i = 0
    while (i < len(listed)):
        first = listed[i][0]
        second = listed[i][1]
        #print("first:", first)
        #print("second:",second)
        count = 0
        if(first == second):
            i += 1
            continue
        another = []
        j = 0
        while(j < len(listed)):
            if(listed[j][0] == second):
                another.append(listed[j])
            j += 1
        k = 0
        #print(another)
        played = False
        while(k < len(another)):
            played = True
            third = another[k][1]
            #print(third)
        
            if(find(listed,first,third) == False):
                return False
                
            k += 1
        i +=1
    return True

def is_antisymmetric (adj_mat) :
    """Determines if the relation is antisymmetric.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    listed = mapToSet(adj_mat)
    i = 0
    while i < len(listed):
        first = listed[i][0]
        second = listed[i][1]
        if(first == second):
            i += 1
        else:
            j = 0
            count = 0
            while j < len(listed):
                f2 = listed[j][0]
                s2 = listed[j][1]
                if(first == s2 and second == f2):
                    if(first != second):
                        return False
                    count += 1
                j += 1
            i += 1
    return True

def is_irreflexive (adj_mat) :
    """Determines if the relation is irreflexive.

    Args:
        adj_mat [list[list[int]]]: an adjacency matrix of the relation, where list[i][j] is 1 if i~j
    Returns:
        meets_definition [bool]

    """
    i = 0
    row = len(adj_mat)
    col = len(adj_mat[0])
    if(row>col):
        while(i<col):
            if(adj_mat[i][i] == 1):
                return False
            i+=1 
    elif(col>row):
        while(i<row):
            if(adj_mat[i][i] == 1):
                return False
            i += 1
    else:
        while(i < len(adj_mat)):    
            if(adj_mat[i][i] == 1):
                return False
            i +=1
        
    return True
    

######################################################################
### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
######################################################################
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 3: Functions!")
    print("#######################################")
    print()
    print("---------------------------------------")
    print("PART A: Function Properties")
    print("---------------------------------------")

    example_1 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:3}] #not anything
    example_2 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:5}] #one to one (nothing else)
    example_3 = [[1 ,2 ,3 ,4],[1,2,3],{1:2, 2:3, 3:1,4:3}] #onto (nothing else)
    example_4 = [[1 ,2 ,3 ,4],[1,2,3,4],{1:2, 2:3, 3:1,4:4}] #bijective
    
    print("---------------------------------------")
    print("\'is_onto\' Tests")
    print("---------------------------------------")
    is_onto_tests = [example_1, example_2, example_3, example_4]
    is_onto_answers = [False, False, True, True]
  
    for count, test in enumerate(is_onto_tests):
        if (is_onto(is_onto_tests[count][0],is_onto_tests[count][1],
                    is_onto_tests[count][2]) == is_onto_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_onto_answers[count]}')
        print(f'Your Answer: {is_onto(is_onto_tests[count][0],is_onto_tests[count][1],is_onto_tests[count][2])}')
        
    print("---------------------------------------")
    print("\'is_one_to_one\' Tests")
    print("---------------------------------------")
    is_one_to_one_tests = [example_1, example_2, example_3, example_4]
    is_one_to_one_answers = [False, True, False, True]
  
    for count, test in enumerate(is_one_to_one_tests):
        if (is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1],
                    is_one_to_one_tests[count][2]) == is_one_to_one_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_one_to_one_answers[count]}')
        print(f'Your Answer: {is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1],is_one_to_one_tests[count][2])}')
    
    print("---------------------------------------")
    print("\'is_bijective\' Tests")
    print("---------------------------------------")
    is_bijective_tests = [example_1, example_2, example_3, example_4]
    is_bijective_answers = [False, False, False, True]
  
    for count, test in enumerate(is_onto_tests):
        if (is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],
                    is_bijective_tests[count][2]) == is_bijective_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_bijective_answers[count]}')
        print(f'Your Answer: {is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],is_bijective_tests[count][2])}')
        
    print()
    print("---------------------------------------")
    print("PART B: Relation Properties")
    print("---------------------------------------")

    example_1 = [[1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1]]
    
    example_2 = [[0, 1, 1, 0, 1],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 1],
                [0, 1, 1, 1, 1],
                [1, 1, 1, 1, 0]]
    
    example_3 = [[0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],]

    example_4 = [[0, 0, 0, 0, 1],
                [0, 1, 1, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 1, 0, 1, 1],
                [1, 1, 1, 0, 1],]
    
    print("---------------------------------------")
    print("\'is_reflexive\' Tests")
    print("---------------------------------------")

    relation_tests = [example_1, example_2, example_3, example_4]
    is_reflexive_answers = [True, False, False, False]
  
    for count, test in enumerate(relation_tests):
        your_answer = is_reflexive(test)
        if (your_answer == is_reflexive_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_reflexive_answers[count]}')
        print(f'Your Answer: {your_answer}')
        
        
    print("---------------------------------------")
    print("\'is_symmetric\' Tests")
    print("---------------------------------------")
    is_symmetric_answers = [True, True, False, False]
  
    for count, test in enumerate(relation_tests):
        your_answer = is_symmetric(test)
        if (your_answer == is_symmetric_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_symmetric_answers[count]}')
        print(f'Your Answer: {your_answer}')
        
        
    print("---------------------------------------")
    print("\'is_transitive\' Tests")
    print("---------------------------------------")
    is_transitive_answers = [True, False, True, False]
  
    for count, test in enumerate(relation_tests):
        your_answer = is_transitive(test)
        if (your_answer == is_transitive_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_transitive_answers[count]}')
        print(f'Your Answer: {your_answer}')