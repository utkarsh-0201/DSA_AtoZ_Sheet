from random import random
from typing import List


class Sorting_Algorithm(object):

    def __init__(self, data: List[int]) -> None:
        self._input_list = data
        self._length = len(data)

    def bubble_sort(self) -> List[int]:
        """
        Bubble sort algorithm
        :return: sorted list
        """
        # Traverse through all array elements
        for i in range(self._length):

            # Last i elements are already in place
            for j in range(0, self._length - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if self._input_list[j] > self._input_list[j + 1]:
                    self._input_list[j], self._input_list[j + 1] = self._input_list[j + 1], self._input_list[j]

        return self._input_list
    
    def insertion_sort(self) -> List[int]:
        """
        Insertion sort algorithm
        :return: sorted list
        """
        # [8, 2, 4, 6, 12, 10]
        for i in range(1, self._length):
            key = self._input_list[i]
            for j in range(i-1 , 0, -1):
                #if self._input_list[j] < key:
                #self._input_list[j], self._input_list[i] = self._input_list[i], self._input_list[j]
                print(f'{i}, {j}Comparing {key} => {self._input_list[j]}', end='')
            print("\n")
        return self._input_list

if __name__ == "__main__":
    # Create random list of int numbers
    data = [int(random() * 100) for _ in range(10)]
    data = [91, 12, 9, 58, 76, 6, 36, 86, 90, 93]
    print(f'List before Sorting> {data}')
    sort_obj = Sorting_Algorithm(data)
    print(f'List after Sorting> {sort_obj.insertion_sort()}')
        

