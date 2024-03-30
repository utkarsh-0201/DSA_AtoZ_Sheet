# Find the maximum element in an array.
# Find the minimum element in an array.
# Calculate the sum of all elements in an array.
# Reverse an array.
# Rotate an array to the right by k steps.
# Find the "Kth" largest and "Kth" smallest element in an array.
# Implement a function to remove duplicates from an array.
# Given an array of integers, find two numbers such that they add up to a specific target number.
# Check if a given array is sorted or not.
# Implement an algorithm to segregate 0s and 1s in an array.


from typing import List


def max_min_element(data: List[int]) -> int:
    """
    Find the largest element in an array.
    :param data: list of integers
    :return: largest element in the array
    """
    max_elem = data[0]
    min_element = data[0]
    for element in data:
        if element > max_elem:
            max_elem = element
        if element < min_element:
            min_element = element
    return max_elem, min_element


def rotate_array(data: List[int], k: int) -> List[int]:
    """
    Rotate an array to the right by k steps.
    :param data: list of integers
    :param k: number of steps
    :return: rotated array
    """
    for i in range(k):
        data.insert(0, data.pop())
    return data

data = [1, 2, 3, 4, 5]
print(max_min_element(data))

k = 2
print(rotate_array(data, k))