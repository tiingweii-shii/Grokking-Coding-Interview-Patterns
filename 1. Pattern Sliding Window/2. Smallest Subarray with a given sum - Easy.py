# Smallest Subarray with a given sum
# Sliding Windows - Easy

'''
Problem Statement #
Given an array of positive numbers and a positive number ‘S’, find the length of the
smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

Approach: add elements until the sum is greater than target, then shrink the window while updating the smallest window size until
the sum is less than the target

'''

# My Solution
def smallest_subarray_with_sum(s, arr):
    if sum(arr) < s:
        return 0
    smallest = len(arr)
    start, windowSum = 0, 0
    for end in range(len(arr)):
        windowSum += arr[end]
        while windowSum >= s:
            smallest = min(smallest, end - start + 1)
            windowSum -= arr[start]
            start += 1
    return smallest
arr1 = [2, 1, 5, 2, 3, 2]
S1 = 7
ans1 = smallest_subarray_with_sum(S1, arr1)
assert ans1 == 2, "Output: " + str(ans1) + " target sum: "+ str(S1) + " should return 2 " + str(arr1) 

arr2 = [2, 1, 5, 2, 8]
S2 = 7
ans2 = smallest_subarray_with_sum(S2, arr2)
assert ans2 == 1, "Output: " + str(ans2) + "  target sum: "+ str(S2) + " should return 1 " + str(arr2)

arr3 = [3, 4, 1, 1, 6]
S3 = 8
ans3 = smallest_subarray_with_sum(S3, arr3)
assert ans3 == 3, "Output: " + str(ans3) + " target sum: "+ str(S3) + " should return 3 " + str(arr3)

arr0 = [3, 4, 6]
S0 = 15
ans0 = smallest_subarray_with_sum(S0, arr0)
assert ans0 == 0, "Output: " + str(ans0) + " target sum: "+ str(S0) + " should return 0 " + str(arr0)

print("ALL TESTS PASSED!")

# Educative.io Solution
import math
def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length

print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(S1, arr1))) # 2
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(S2, arr2))) # 1
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(S3, arr3))) # 3
