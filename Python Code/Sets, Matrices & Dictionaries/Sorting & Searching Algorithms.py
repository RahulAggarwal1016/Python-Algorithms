"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Sort arrays using the various methods below
"""

#Linear Search Function

def linearSearch(target, array):
    """
    Input:
    Param -- Takes in two arguements, an integer (target) and a list (array)
    Output:
    Return -- A singular integer type value
    Purpose:
    To find the index location of target in array
    """

    counter = 0

    for i in array:
	    if i == target:
		    return counter
	    counter += 1
    else:
	    return -1

#Binary Search

def binarySearch(target,array):

    """
    Input:
    Param -- Takes in two arguements, an integer (target) and a list (array)
    Output:
    Return -- A singular integer type value (middle)
    Purpose:
    To find the index location of "target" in "array"
    """

    left = 0
    right = len(array) - 1

    while left < right:
        middle = (left + right)//2
        if array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
        else:
            return middle 

#Bubble Sort

def bubbleSort(array):

    """
    Input:
    Param -- Takes in one arguement, a list (array)
    Output:
    Return -- Returns a list type value (array)
    Purpose:
    To sort the list "array" from least to greatest
    """

    swapped = True

    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                temp = array[i-1]
                array.remove(temp)
                array.insert(i,temp)
                swapped = True

    return array

#Insertion Sort

def insertionSort(array):

    """
    Input:
    Param -- Takes in one arguement, a list (array)
    Output:
    Return -- A singular list type value (array)
    Purpose:
    To sort the list "array" from least to greatest
    """

    i = 1
    while i < len(array):
        j = i
        while j > 0 and array[j-1] > array[j]:
            temp = array[j-1]
            array.remove(temp)
            array.insert(j,temp)
            j -= 1
        i += 1
    
    return array

#Selection Sort

def selectionSort(array, new_array = []):

    """
    Input:
    Param -- Takes in one arguement, a list (array)
    Output:
    Return -- A list type value (new_array)
    Purpose:
    To sort the list "array" from least to greatest
    """

    while len(array) != 0:
        minimum = min(array)
        new_array.append(minimum)
        array.remove(minimum)

    return new_array

#Merge Sort

def combine(left, right):

    """
    Input:
    Param -- Takes in two arguments, two list type values (left and right)
    Output:
    Return -- A list type value (result)
    Purpose:
    To sort combine left and right while sorting the combined list 
    """

    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])

    while left:
        result.append(left[0])
        left.remove(left[0])
    while right:
        result.append(right[0])
        right.remove(right[0])
    
    return result

def mergeSort(array):
    
    """
    Input:
    Param -- Takes in a singular list type value (array)
    Output:
    Return -- A list type value (array)
    Purpose:
    To sort array from least to greatest using the combine function recursively
    """

    if len(array) <= 1:
	    return array

    left = []
    right = []

    middle = len(array)//2

    left = array[:middle]
    right = array[middle:]

    left = mergeSort(left)
    right = mergeSort(right)

    return combine(left, right)