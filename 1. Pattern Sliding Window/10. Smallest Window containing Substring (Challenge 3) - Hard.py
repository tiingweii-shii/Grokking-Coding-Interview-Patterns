# Problem Challenge 3: Smallest Window containing Substring
# Sliding Windows - Hard

'''
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:
Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".

Example 3:
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
'''

# Sample Inputs and Outputs -------------------------------------------------------------
str1 = "aabdec"
pattern1 = "abc"
output1 = "abdec"

str2 = "abdabca"
pattern2 = "abc"
output2 = "abc"

str3 = "adcad"
pattern3 = "abc"
output3 = ""

str4 = "aaacdbbca"
pattern4 = "abc"
output4 = "bca"

str5 = "abcaxcbd"
pattern5 = "abcd"
output5 = "axcbd"

strs = [str1, str2, str3, str4, str5]
patterns = [pattern1, pattern2, pattern3, pattern4, pattern5]
expected_outputs = [output1, output2, output3, output4, output5]

# My Solution ---------------------------------------------------------------------------

import collections
def find_substring(s, pattern):
    pattern_map = collections.Counter(pattern)
    start, end = 0, 0
    minLengthStart, minLength, matched = 0, len(s) + 1, 0

    while end < len(s):
        if s[end] in pattern_map:
            pattern_map[s[end]] -= 1
            if pattern_map[s[end]] == 0:
                matched += 1
            
            while matched == len(pattern_map):
                if end - start + 1 < minLength:
                    minLength = end - start + 1
                    minLengthStart = start
                if s[start] in pattern_map:
                    if pattern_map[s[start]] == 0:
                        matched -= 1
                    pattern_map[s[start]] += 1
                start += 1
        end += 1

    if minLength > len(s):
        return ""
    return s[minLengthStart:minLengthStart + minLength]
# Tests


def test_my_solution():
    for i in range(len(strs)):
        output = find_substring(strs[i], patterns[i])
        assert output == expected_outputs[i], "Test" + str(i + 1) + " Output: " + str(
            output) + " str " + strs[i] + " pattern: " + patterns[i] + " should return " + str(expected_outputs[i])
    print("My Solution: ALL TESTS PASSED!")


test_my_solution()

# Educative.io Solution ----------------------------------------------------------------
'''
This problem follows the Sliding Window pattern and has a lot of similarities with Permutation in a String with one difference. In this problem, we need to find a substring having all characters of the pattern which means that the required substring can have some additional characters and doesn’t need to be a permutation of the pattern. Here is how we will manage these differences:

We will keep a running count of every matching instance of a character.
Whenever we have matched all the characters, we will try to shrink the window from the beginning, keeping track of the smallest substring that has all the matching characters.
We will stop the shrinking process as soon as we remove a matched character from the sliding window. One thing to note here is that we could have redundant matching characters, e.g., we might have two ‘a’ in the sliding window when we only need one ‘a’. In that case, when we encounter the first ‘a’, we will simply shrink the window without decrementing the matched count. We will decrement the matched count when the second ‘a’ goes out of the window.

Time Complexity
The time complexity of the above algorithm will be O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity #
The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. In the worst case, we also need O(N) space for the resulting substring, which will happen when the input string is a permutation of the pattern.
'''

def find_substring_educative(str, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str) + 1
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0: # Count every matching of a character
                matched += 1

        # shrink the window if we can, finish as sson as we remove a matched character
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                # Note that we could have redundant matching characters, therefore we'll decrement the matched count only when a useful occurrence of a matched character is going out of the window
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    
    if min_length > len(str):
        return ""
    return str[substr_start:substr_start + min_length]

# Tests
def test_educative_solution():
    for i in range(len(strs)):
        output = find_substring_educative(strs[i], patterns[i])
        assert output == expected_outputs[i], "Test" + str(i + 1) + " Output: " + str(
            output) + " str " + strs[i] + " pattern: " + patterns[i] + " should return " + str(expected_outputs[i])
    print("Educative.io Solution: ALL TESTS PASSED!")

test_educative_solution()