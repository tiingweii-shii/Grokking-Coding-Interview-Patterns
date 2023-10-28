# Problem Challenge 2: String Anagrams
# Sliding Windows - Hard

'''
Given a string and a pattern, find all anagrams of the pattern in the given
string.

Anagram is actually a Permutation of a string. For example, “abc” has the
following six anagrams:
1. abc
2. acb
3. bac
4. bca
5. cab
6. cba
Write a function to return a list of starting indices of the anagrams of the
pattern in the given string.

Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca",
"cab", and "abc".
'''

# Sample Inputs and Outputs -------------------------------------------------------------
str1 = "ppqp"
pattern1 = "pq"
output1 = [1, 2]

str2 = "abbcabc"
pattern2 = "abc"
output2 =  [2, 3, 4]

str3 = "bcdxabcdyb"
pattern3 = "bcdyabcdx"
output3 = [0, 1]

str4 = "aaacbbca"
pattern4 = "abc"
output4 = [2, 5]

str5 = "abcacbd"
pattern5 = "abcd"
output5 = [3]

str6 = "abcdacbbdcba"
pattern6 = "abcd"
output6 = [0, 1, 3, 8]

str7 = "abcacbbdcb"
pattern7 = "abcd"
output7 = []

strs = [str1, str2, str3, str4, str5, str6, str7]
patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7]
expected_outputs = [output1, output2, output3, output4, output5, output6, output7]

# My Solution ---------------------------------------------------------------------------
# This problem is very similar to challenge 1, but instead of returning True
# when we find a match, we append the start index to the result array
# Time Complexity: O(N + M), N = len(s), M = len(pattern)
# Space Complexity: O(N) for the result list, O(M) for pattern_map
import collections
def find_string_anagrams(s, pattern):
    matched = 0
    start = 0
    pattern_map = collections.Counter(pattern)
    res = []

    for end in range(len(s)):
        if s[end] in pattern_map:
            pattern_map[s[end]] -= 1
            if pattern_map[s[end]] == 0:
                matched += 1
                if matched == len(pattern_map):
                    res.append(start)
        if end - start + 1 == len(pattern):
            if s[start] in pattern_map:
                if pattern_map[s[start]] == 0:
                    matched -= 1
                pattern_map[s[start]] += 1
            start += 1
    return res

# Tests
def test_my_solution():
    for i in range(len(strs)):
        output = find_string_anagrams(strs[i], patterns[i])
        assert output == expected_outputs[i], "Test" + str(i + 1) + " Output: " + str(output) + " str " + strs[i] + " pattern: " + patterns[i] + " should return " + str(expected_outputs[i])
    print("My Solution: ALL TESTS PASSED!")
test_my_solution()

# Educative.io Solution ----------------------------------------------------------------
'''
This problem follows the Sliding Window pattern and is very similar to
Permutation in a String. In this problem, we need to find every occurrence of
any permutation of the pattern in the string. We will use a list to store the
starting indices of the anagrams of the pattern in the string.

Time Complexity
The time complexity of the above algorithm will be O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity
The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. In the worst case, we also need O(N) space for the result list, this will happen when the pattern has only one character and the string contains only that character.
'''
def find_string_anagrams_educative(str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    result_indices = []
    # our goal is to match all the characters from the 'char_frequency' with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matached character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            result_indices.append(window_start)

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return result_indices

# Tests
def test_educative_solution():
    for i in range(len(strs)):
        output = find_string_anagrams_educative(strs[i], patterns[i])
        assert output == expected_outputs[i], "Test" + str(i + 1) + " Output: " + str(output) + " str " + strs[i] + " pattern: " + patterns[i] + " should return " + str(expected_outputs[i])
    print("Educative.io Solution: ALL TESTS PASSED!")
test_educative_solution()
