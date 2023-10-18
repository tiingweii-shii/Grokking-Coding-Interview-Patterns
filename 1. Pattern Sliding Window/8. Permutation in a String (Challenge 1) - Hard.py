# Problem Challenge 1: Permutation in a String
# Sliding Windows - Hard

'''
Given a string and a pattern, find out if the string contains any permutation of
the pattern.

Permutation is defined as the re-arranging of the characters of the string. For
example, “abc” has the following six permutations:
1. abc
2. acb
3. bac
4. bca
5. cab
6. cba
If a string has ‘n’ distinct characters it will have n! permutations.

Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
'''

# Sample Inputs and Outputs -------------------------------------------------------------
str1 = "oidbcaf"
pattern1 = "abc"
output1 = True

str2 = "odicf"
pattern2 = "dc"
output2 =  False

str3 = "bcdxabcdy"
pattern3 = "bcdyabcdx"
output3 = True

str4 = "aaacb"
pattern4 = "abc"
output4 = True

str5 = "abcacbd"
pattern5 = "abcd"
output5 = True

str6 = "abcacbbdcba"
pattern6 = "abcd"
output6 = True

str7 = "abcacbbdcb"
pattern7 = "abcd"
output7 = False

strs = [str1, str2, str3, str4, str5, str6, str7]
patterns = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7]
expected_outputs = [output1, output2, output3, output4, output5, output6, output7]

# My Solution ---------------------------------------------------------------------------
# I struggled with this one, so I looked at Educative.io's Solution. Some notes here:
# - The size of the sliding window is fixed: we move the start to the right by one everytime the window has the same length as the pattern.
# - Because we know our window has the right size at every iteration, we can safely return True if we have the correct number of matches
# - Keeping track of 'matched' can help us avoid checking the frequency of each char in the map - the frequency can go to negative, but that
#   makes it impossible for the 'matched' to reach the correct number because we have a fixed window size
import collections
def find_permutation(s, pattern):
    matched = 0
    start = 0
    hashmap = collections.Counter(pattern)
    
    for end in range(len(s)):
        if s[end] in hashmap:
            hashmap[s[end]] -= 1
            if hashmap[s[end]] == 0:
                matched += 1
                if matched == len(hashmap):
                    return True
        if end - start + 1 == len(pattern):
            if s[start] in hashmap:
                if hashmap[s[start]] == 0:
                    matched -= 1
                hashmap[s[start]] += 1
            start += 1
    return False

# Tests
def test_my_solution():
    for i in range(len(strs)):
        output = find_permutation(strs[i], patterns[i])
        assert output == expected_outputs[i], "Test" + str(i + 1) + " Output: " + str(output) + " str " + strs[i] + " pattern: " + patterns[i] + " should return " + str(expected_outputs[i])
    print("My Solution: ALL TESTS PASSED!")
test_my_solution()

# Educative.io Solution ----------------------------------------------------------------
'''
This problem follows the Sliding Window pattern and we can use a similar sliding
window strategy as discussed in Longest Substring with K Distinct Characters. We
can use a HashMap to remember the frequencies of all characters in the given
pattern. Our goal will be to match all the characters from this HashMap with a
sliding window in the given string. Here are the steps of our algorithm:

 1. Create a HashMap to calculate the frequencies of all characters in the pattern.
 2. Iterate through the string, adding one character at a time in the sliding window.
 3. If the character being added matches a character in the HashMap, decrement
    its frequency in the map. If the character frequency becomes zero, we got a
    complete match.
 4. If at any time, the number of characters matched is equal to the number of
    distinct characters in the pattern (i.e., total characters in the HashMap),
    we have gotten our required permutation.
 5. If the window size is greater than the length of the pattern, shrink the
    window to make it equal to the size of the pattern. At the same time, if the
    character going out was part f the pattern, put it back in the frequencyHashMap.

Time Complexity
The time complexity of the above algorithm will be O(N+M) where ‘N’ and ‘M’ are
the number of characters in the input string and the pattern respectively.

Space Complexity
The space complexity of the algorithm is O(M) since in the worst case, the whole
pattern can have distinct characters which will go into the HashMap.
'''
def find_permutation_educative(str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

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
            return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return False
    
# Tests
def test_educative_solution():
    for i in range(len(strs)):
        output = find_permutation_educative(strs[i], patterns[i])
        assert output == expected_outputs[i], "Test" + str(i + 1) + " Output: " + str(output) + " str " + strs[i] + " pattern: " + patterns[i] + " should return " + str(expected_outputs[i])
    print("Educative.io Solution: ALL TESTS PASSED!")
test_educative_solution()
                
