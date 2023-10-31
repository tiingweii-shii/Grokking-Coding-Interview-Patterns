# Remove Duplicates
# Two Pointers - Easy

'''
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''

input1 = [2, 3, 3, 3, 6, 9, 9]
output1 = 4

input2 = [2, 2, 2, 11]
output2 = 2

input3 = [1, 1, 3, 3, 4, 4, 5, 5]
output3 = 4

inputs = [input1, input2, input3]
expected_outputs = [output1, output2, output3]

# My Solution ---------------------------------------------------------------------------
# Note: I did not modify the array in place as requested
def remove_duplicates(arr):
    length = len(arr)

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            length -= 1
    return length

# Tests
def test_my_solution():
    for i in range(len(inputs)):
        output = remove_duplicates(inputs[i])
        assert output == expected_outputs[i], "Test" + str(i) + " Output: " + str(output) + " input " + str(inputs[i]) + " should return " + str(expected_outputs[i])
    print("My Solution: ALL TESTS PASSED!")
test_my_solution()

# Educative.io Solution ----------------------------------------------------------------
'''
In this problem, we need to remove the duplicates in-place such that the resultant length of the array remains sorted. As the input array is sorted, therefore, one way to do this is to shift the elements left whenever we encounter duplicates. In other words, we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number. So our algorithm will be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we’ve seen.
'''
