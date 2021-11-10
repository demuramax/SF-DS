"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def binary_search(number):
    low = 1
    high = 100
    # количество попыток
    count = 0
    while low <= high:
        mid = int((low + high)/2) # if the number is not even it woule be rounded to the smaller one.
        # guess = nums_list[mid]
        count += 1
        if mid == number:
            return mid, count
        if mid > number:
            high = mid - 1
        else: 
            low = mid + 1
    return None
    
print(binary_search(number))