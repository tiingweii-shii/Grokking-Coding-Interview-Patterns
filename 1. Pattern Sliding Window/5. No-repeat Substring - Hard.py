# No-repeat Substring
# Sliding Windows - Hard

'''
Problem Statement #
Given a string, find the length of the longest substring which has no
repeating characters.

Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".

My Examples:
Example 4:
Input: String="abccdea"
Output: 4

Example 5:
Input: String="aaaaaaaa"
Output: 1
'''
# Sample Inputs and Outputs -------------------------------------------------------------
input1 = "aabccbb"
output1 = 3

input2 = "abbbb"
output2 = 2

input3 = "abccde"
output3 = 3

input4 = "abccdea"
output4 = 4

input5 = "aaaaaaaa"
output5 = 1

input5 = "aphbcabdgef"
output5 = 7


# My Solution ---------------------------------------------------------------------------
# Hashmap to keep track of seen characters and their index (last seen)
# To process a character we have seen before, update the start of the
# window to be the right of its last seen index Note that if a character
# in the hashmap's index < start of the window, it is considered not
# seen since its not in the slinding window

# Time Complexity: O(N)
# Space Complexity: O(K) - K is the number of distinct characters

def non_repeat_substring(s):
    max_len = 0
    # Hashmap to keep track of seen characters and their index (last seen)
    chars_map = {}
    start = 0
    for end in range(len(s)):
        if s[end] in chars_map and chars_map[s[end]] >= start:
            max_len = max(max_len, end - start)
            start = chars_map[s[end]] + 1
        chars_map[s[end]] = end
    return max(max_len, end - start + 1)

# Tests
def test_my_solution():
    inputs = [input1, input2, input3, input4, input5]
    expected_outputs = [output1, output2, output3, output4, output5]
    for i in range(len(inputs)):
        output = non_repeat_substring(inputs[i])
        assert output == expected_outputs[i], "Output: " + str(output) + " string " + inputs[i] + " should return " + str(expected_outputs[i])
    print("My Solution: ALL TESTS PASSED!")
test_my_solution()

# Note: My solution is similar to the Educative.io Solution on a high
# level, they differ in implementation details, specifically how they
# handle characters which have been seen and when to update the max_len.

# Educative.io Solution ----------------------------------------------------------------
'''
This problem follows the Sliding Window pattern and we can use a similar
dynamic sliding window strategy as discussed in Longest Substring with K
Distinct Characters. We can use a HashMap to remember the last index of
each character we have processed. Whenever we get a repeating character
we will shrink our sliding window to ensure that we always have distinct
characters in the sliding window.

Time Complexity: The time complexity of the above algorithm will be O(N)
where ‘N’ is the number of characters in the input string.

Space Complexity:
The space complexity of the algorithm will be O(K) where K is the number
of distinct characters in the input string. This also means K<=N,
because in the worst case, the whole string might not have any repeating
character so the entire string will be added to the HashMap. Having said
that, since we can expect a fixed set of characters in the input string
(e.g., 26 for English letters), we can say that the algorithm runs in
fixed space O(1); in this case, we can use a fixed-size array instead of
the HashMap.
'''
def non_repeat_substring_educative(s):
    window_start = 0
    max_length = 0
    char_index_map = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(s)):
        right_char = s[window_end]
        # if the map already contains the 'right_char', shrink the window from the beginning so that we have only one occurrence of 'right_char'
        if right_char in char_index_map:
            # this is tricky: in the current window, we will not have any 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
            window_start = max(window_start, char_index_map[right_char] + 1)
        # insert the 'right_char' into the map
        char_index_map[right_char] = window_end
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
    
# Tests
def test_educative_solution():
    inputs = [input1, input2, input3, input4, input5]
    expected_outputs = [output1, output2, output3, output4, output5]
    for i in range(len(inputs)):
        output = non_repeat_substring_educative(inputs[i])
        assert output == expected_outputs[i], "Output: " + str(output) + " string " + inputs[i] + " should return " + str(expected_outputs[i])
    print("Educative.io Solution: ALL TESTS PASSED!")
test_educative_solution()
