from itertools import permutations
import math


def if_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    permutated_numbers = []
    for i in range(1, len(numbers) + 1):
        permutated_numbers += list(permutations(numbers, i))

    num_list = []
    for nums in permutated_numbers:
        num_string = ""
        for i in nums:
            num_string += i
        num = int(num_string)
        if num not in num_list:
            if if_prime(num):
                num_list.append(num)
    return len(num_list)
