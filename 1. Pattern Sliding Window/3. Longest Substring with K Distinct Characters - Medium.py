# Longest Substring with K Distinct Characters
# Sliding Windows - Medium

'''
Problem Statement #
Given a string, find the length of the longest substring in it
with no more than K distinct characters.

Example 0:
Input: String="araraci", K=2
Output: 5
Explanation: The longest substring with no more than '2' distinct characters is "arara".


Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''

# My Solution
# HashMap to keep track of current distinct chars with the index of its last occurance
# When shrinking the sliding window, we update the start with (the earliest last occurence + 1) and del that char from the map
# delete_char_with_earliest_last_occurance() is O(K) - overall running time is O(N * K), space O(K)
def longest_substring_with_k_distinct_chars(s, k):
    # keep track of current distinct chars, char: index of the last occurance
    seen = {}
    max_len = 0
    start = 0

    def delete_char_with_earliest_last_occurance():
        # character with the earliest *last occurance*
        earliest = len(s)
        earliest_char = None
        for c in seen:
            if seen[c] < earliest:
                earliest = seen[c]
                earliest_char = c
        del seen[earliest_char]
        return earliest

    for end in range(len(s)):
        if not (s[end] in seen or len(seen) < k):
            # update max_len
            max_len = max(max_len, end - start)
            start = delete_char_with_earliest_last_occurance() + 1
        seen[s[end]] = end
    return max_len

s0 = "araraci"
k0 = 2
ans0 = longest_substring_with_k_distinct_chars(s0, k0)
expected_ans0 = 5
assert ans0 == expected_ans0, "Output: " + str(ans0) + " k = " + str(k0) + " in " + s0 + " should return " + str(expected_ans0)

s1 = "araaci"
k1 = 2
ans1 = longest_substring_with_k_distinct_chars(s1, k1)
expected_ans1 = 4
assert ans1 == expected_ans1, "Output: " + str(ans1) + " k = " + str(k1) + " in " + s1 + " should return " + str(expected_ans1)

s2 = "araaci"
k2 = 1
ans2 = longest_substring_with_k_distinct_chars(s2, k2)
expected_ans2 = 2
assert ans2 == expected_ans2, "Output: " + str(ans2) + " k = " + str(k2) + " in " + s2 + " should return " + str(expected_ans2)

s3 = "cbbebi"
k3 = 3
ans3 = longest_substring_with_k_distinct_chars(s3, k3)
expected_ans3 = 5
assert ans3 == expected_ans3, "Output: " + str(ans3) + " k = " + str(k3) + " in " + s3 + " should return " + str(expected_ans3)  

print("My Solution: ALL TESTS PASSED!")

# Educative.io Solution
# HashMap to keep track of the freq of each character in the window
# When shrinking the window, keep moving the start to the right while decrementing the freq count until we have k characters in the map
# Time Complexity: O(N) - while loop processes each character only once - O(N + N) = O(N)
# Space Complexity: O(K)
def longest_substring_with_k_distinct(s, k):
    start = 0
    max_len = 0
    char_freq = {}

    for end in range(len(s)):
        end_char = s[end]
        if end_char not in char_freq:
            char_freq[end_char] = 0
        char_freq[end_char] += 1

        while len(char_freq) > k:
            start_char = s[start]
            char_freq[start_char] -= 1
            if char_freq[start_char] == 0:
                del char_freq[start_char]
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len
ans0 = longest_substring_with_k_distinct(s0, k0)
assert ans0 == expected_ans0, "Output: " + str(ans0) + " k = " + str(k0) + " in " + s0 + " should return " + str(expected_ans0)

ans1 = longest_substring_with_k_distinct(s1, k1)
assert ans1 == expected_ans1, "Output: " + str(ans1) + " k = " + str(k1) + " in " + s1 + " should return " + str(expected_ans1)

ans2 = longest_substring_with_k_distinct(s2, k2)
assert ans2 == expected_ans2, "Output: " + str(ans2) + " k = " + str(k2) + " in " + s2 + " should return " + str(expected_ans2)

ans3 = longest_substring_with_k_distinct(s3, k3)
assert ans3 == expected_ans3, "Output: " + str(ans3) + " k = " + str(k3) + " in " + s3 + " should return " + str(expected_ans3)  

print("Educative.io Solution: ALL TESTS PASSED!")
