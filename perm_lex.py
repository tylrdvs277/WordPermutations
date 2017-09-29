# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Assignment 1
# Term:        Fall 2017

def perm_gen_lex(string): 
    """Python program to generate all the permutations 
    of the characters in a string in lexicographic order"""
    letters = [letter for letter in string]
    if len(string) <= 1:
        return letters
    permutations = []
    for idx in range(len(string)):
        first = letters.pop(idx)
        for permutation in perm_gen_lex("".join(letters)): 
        	permutations.append(first + permutation)       
        letters.insert(idx, first)
    return ["".join(permutation) for permutation in permutations]