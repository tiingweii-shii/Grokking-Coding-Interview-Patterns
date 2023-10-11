# Longest Subarray with Ones after Replacement
# Sliding Windows - Hard

'''
Problem Statement #
Given an array containing 0s and 1s, if you are allowed to replace no more than
‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous
subarray of 1s having length 6.

Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest
contiguous subarray of 1s having length 9.
'''
# Sample Inputs and Outputs -------------------------------------------------------------
arr1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k1 = 2
output1 = 6

arr2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k2 = 3
output2 = 9

arr3 = [1, 1, 1, 1, 1]
k3 = 1
output3 = 5

arr4 = [0, 0, 0, 0, 0]
k4 = 1
output4 = 1

arr5 = [1, 1, 1, 0, 1, 1, 1]
k5 = 0
output5 = 3

arrs = [arr1, arr2, arr3, arr4, arr5]
ks = [k1, k2, k3, k4, k5]
expected_outputs = [output1, output2, output3, output4, output5]

# My Solution ---------------------------------------------------------------------------
# This problem is very similar to Longest Substring with same Letters after
# Replacement. Here, we extend the sliding window while keeping track of number
# of 0s (to replace) in the window, when the number of 0s exceeds k, we shrink
# the sliding window - keep moving the start pointer to the right until we no
# longer have more than k 0s.

# Time Complexity: O(N)
# Space Complexity: O(1)
def length_of_longest_subarr(arr, k):
    max_len = 0
    start = 0
    # number of 0s to replace in the sliding window
    num_replacements = 0

    for end in range(len(arr)):
        if arr[end] == 0:
            num_replacements += 1
            while num_replacements > k:
                if arr[start] == 0:
                    num_replacements -= 1
                start += 1
        max_len = max(max_len, end - start + 1)
    return max_len

# Tests
def test_my_solution():
    for i in range(len(arrs)):
        output = length_of_longest_subarr(arrs[i], ks[i])
        assert output == expected_outputs[i], "Test" + str(i) + " Output: " + str(output) + " arr " + str(arrs[i]) + " k:" + str(ks[i]) + " should return " + str(expected_outputs[i])
    print("My Solution: ALL TESTS PASSED!")
test_my_solution()

# Educative.io Solution ----------------------------------------------------------------
'''
This problem follows the Sliding Window pattern and is quite similar to Longest
Substring with same Letters after Replacement. The only difference is that, in
the problem, we only have two characters (1s and 0s) in the input arrays.

Following a similar approach, we’ll iterate through the array to add one number
at a time in the window. We’ll also keep track of the maximum number of
repeating 1s in the current window (let’s call it maxOnesCount). So at any time,
we know that we can have a window which has 1s repeating maxOnesCount time, so
we should try to replace the remaining 0s. If we have more than ‘k’ remaining
0s, we should shrink the window as we are not allowed to replace more than ‘k’ 0s.

Time Complexity
The time complexity of the above algorithm will be O(N) where ‘N’ is the count
of numbers in the input array.

Space Complexity
The algorithm runs in constant space O(1).
'''
def length_of_longest_subarr_educative(arr, k):
    window_start, max_length, max_ones_count = 0, 0, 0

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        # Current window size is from window start to window_end, overall we
        # have a maximum of 1s repeating 'max_ones_count' times, this means we
        # can have a window which has 'max_ones_count' 1s and the remaining are
        # 0s which should be repaced with 1s. Now, if the remaining 1s are more
        # than 'k', it is the time to shrink the window as we are not allowed to
        # replace more than 'k' 0s.
        if window_end - window_start + 1 - max_ones_count > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

# Tests
def test_educative_solution():
    for i in range(len(arrs)):
        output = length_of_longest_subarr_educative(arrs[i], ks[i])
        assert output == expected_outputs[i], "Test" + str(i) + " Output: " + str(output) + " arr " + str(arrs[i]) + " k:" + str(ks[i]) + " should return " + str(expected_outputs[i])
    print("Educative.io Solution: ALL TESTS PASSED!")
test_educative_solution()

