# Maximum Sum Subarray of Size K
# Sliding Windows - Easy

'''
Problem Statement
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def max_subarray_sum(k, arr):
    maxSum = 0
    windowSum, windowStart = 0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum
arr1 = [2, 1, 5, 1, 3, 2]
k1 = 3
ans1 = max_subarray_sum(k1, arr1)
assert ans1 == 9, "Output: " + str(ans1) + " window size: "+ str(k1) + " should return 9 " + str(arr1) 

arr2 = [2, 3, 4, 1, 5]
k2 = 2
ans2 = max_subarray_sum(k2, arr2)
assert ans2 == 7, "Output: " + str(ans2) + " window size: "+ str(k2) + " should return 7 " + str(arr2)

print("ALL TESTS PASSED!")
