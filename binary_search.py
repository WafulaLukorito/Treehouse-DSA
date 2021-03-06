
#*Logarithmic Runtime due to while loop, while redefining first and last which grow smaller and smaller.
#* Time Complexity O(logN)
#*Space Complexity  O(1) Constant space
"""[Linear search iterates through all the elements and compares them with the key which has to be searched.
Binary search wisely decreases the size of the array which has to be searched and compares the key with mid element every time.]
    """


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2  #* floor division

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Targer not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # *Has to be sorted!

result = binary_search(numbers, 9)
verify(result)
