def perm_gen_lex(string): 
    # Python program to generate all the permutations 
    # of the characters in a string in lexicographic order 
    letters = [letter for letter in string]
    #copies the string into a list of strings to allow for manipulation
    if len(string) <= 1:
    # Elementary case 
    # Returns a list with a string containing a single letter
        return letters
    permutations = []
    for idx in range(len(string)):
        first = letters.pop(idx)
        # Removes the character to be put first as part of the algorithm
        for permutation in perm_gen_lex("".join(letters)): 
        # Recursive call (permutes the simpler string)
        	permutations.append(first + permutation)       
                # Adds the simpler permutations to the first letter
        letters.insert(idx, first)
        # Ensures the indicies remain consistent over multiple iterations
    return ["".join(permutation) for permutation in permutations] 
    # Returns a list of permuted strings
