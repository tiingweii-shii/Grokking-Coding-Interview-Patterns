# Longest Substring with Same Letters after Replacement
# Sliding Windows - Hard

'''
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no
more than ‘k’ letters with any letter, find the length of the longest substring
having the same letters after replacement.

Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''
# Sample Inputs and Outputs -------------------------------------------------------------
string1 = "aabccbb"
k1 = 2
output1 = 5

string2 = "abbcb"
k2 = 1
output2 = 4

string3 = "abccde"
k3 = 1
output3 = 3

string4 = "abcde"
k4 = 1
output4 = 2

string5 = "aaaaaaaa"
k5 = 3
output5 = 8

string6 = "pahbcababdgef"
k6 = 4
output6 = 7

string7 = "abcdefc"
k7 = 4
output7 = 6

strings = [string1, string2, string3, string4, string5, string6, string7]
ks = [k1, k2, k3, k4, k5, k6, k7]
expected_outputs = [output1, output2, output3, output4, output5, output6, output7]
# My Solution ---------------------------------------------------------------------------
# I couldn't come up with my own solution, so this is just my
# implementation of the Educative.io's solution, which you can read more
# about in the next section.
def length_of_longest_substring(string, k):
    start = 0
    max_length = 0
    # the count of the most repeated character in the window
    max_repeat_count = 0
    char_freq = {}

    for end in range(len(string)):
        end_char = string[end]
        if end_char not in char_freq:
            char_freq[end_char] = 0
        char_freq[end_char] += 1
        max_repeat_count = max(max_repeat_count, char_freq[end_char])

        # shrink the window if we need to replace more than k characters in the window
        if end - start + 1 - max_repeat_count > k:
            start_char = string[start]
            char_freq[start_char] -= 1
            start += 1
            
        max_length = max(max_length, end - start + 1)
    return max_length

# Tests
def test_my_solution():
    for i in range(len(strings)):
        output = length_of_longest_substring(strings[i], ks[i])
        assert output == expected_outputs[i], "Test" + str(i) + " Output: " + str(output) + " string " + strings[i] + " k:" + str(ks[i]) + " should return " + str(expected_outputs[i])
    print("My Solution: ALL TESTS PASSED!")
test_my_solution()

# Educative.io Solution ----------------------------------------------------------------
'''
This problem follows the Sliding Window pattern and we can use a similar dynamic
sliding window strategy as discussed in No-repeat Substring. We can use a
HashMap to count the frequency of each letter.

We’ll iterate through the string to add one letter at a time in the window.
We’ll also keep track of the count of the maximum repeating letter in any window
(let’s call it maxRepeatLetterCount). So at any time, we know that we can have a
window which has one letter repeating maxRepeatLetterCount times, this means we
should try to replace the remaining letters. If we have more than ‘k’ remaining
letters, we should shrink the window as we are not allowed to replace more than
‘k’ letters.

Time Complexity
The time complexity of the above algorithm will be O(N) where ‘N’ is the number
of letters in the input string.

Space Complexity
As we are expecting only the lower case letters in the input string, we can
conclude that the space complexity will be O(26), to store each letter’s
frequency in the HashMap, which is asymptotically equal to O(1).
'''
def length_of_longest_substring_educative(s, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])

        # Current window size is from window start to window_end, overall we
        # have a letter which is repeating 'max_repeat_letter_count' times, this
        # means we can have a window which has one letter repeating
        # 'max_repeat_letter_count' times and the remaining letters we should
        # replace. if the remaining letters are more than 'k', it is the time to
        # shrink the window as we are not allowed to replace more than 'k' letters
        if window_end - window_start + 1 - max_repeat_letter_count > k:
            left_char = s[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

# Tests
def test_educative_solution():
    for i in range(len(strings)):
        output = length_of_longest_substring_educative(strings[i], ks[i])
        assert output == expected_outputs[i], "Test" + str(i) + " Output: " + str(output) + " string " + strings[i] + " k:" + str(ks[i]) + " should return " + str(expected_outputs[i])
    print("Educative.io Solution: ALL TESTS PASSED!")
test_educative_solution()

            
