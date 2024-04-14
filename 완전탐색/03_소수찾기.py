import itertools, math

def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def solution(numbers):
    answer = []
    nums = []

    for i in range(1, len(numbers) + 1):
        permutations = list(itertools.permutations(numbers, i))
        for p in permutations:
            nums.append(int(''.join(p)))

    nums = set(nums)

    for num in nums:
        if isPrime(num):
            answer.append(num)

    return len(answer)
