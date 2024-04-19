from itertools import product

def solution(word):
    answer = 0
    result = []
    
    for i in range(1, 6):
        dup_permutations = list(product(["A", "E", "I", "O", "U"], repeat=i))
        for permutation in dup_permutations:
            result.append(''.join(p for p in permutation))
    
    result.sort()
    answer = result.index(word) + 1
    
    return answer
