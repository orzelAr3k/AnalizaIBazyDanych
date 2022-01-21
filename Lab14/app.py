from copy import deepcopy
from typing import Union

def bubble_sort(lst):
    if len(lst) < 1 or not all(isinstance(x, (int, float)) for x in lst):
        return None
    else:
        sorted_list = deepcopy(lst)
        has_swapped = True

        num_of_iterations = 0

        while(has_swapped):
            has_swapped = False
            for i in range(len(sorted_list) - num_of_iterations - 1):
                if sorted_list[i] > sorted_list[i+1]:
                    # Swap
                    sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
                    has_swapped = True
            num_of_iterations += 1
        
        return sorted_list


lst = [1, 2, 3, 4]
print(bubble_sort(lst))