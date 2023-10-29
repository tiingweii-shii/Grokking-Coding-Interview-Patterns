# Problem Challenge 4: Words Concatenation
# Sliding Windows - Hard

'''
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example 1:
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:
Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".

Example 3:
Input: String="foxfox", Words=["cat", "fox"]
Output: []
'''

# Sample Inputs and Outputs -------------------------------------------------------------
str1 = "catfoxcat"
words1 = ["cat", "fox"]
output1 = [0, 3]

str2 = "catcatfoxfox"
words2 = ["cat", "fox"]
output2 = [3]

str3 = "foxfox"
words3 = ["cat", "fox"]
output3 = []

str4 = "ttttomatotomatotomatommmtomatotomtt"
words4 = ["tomato", "tomato"]
output4 = [3, 9]

str5 = "bbabbaabb"
words5 = ["bba", "abb"]
output5 = [3]

str6 = "bcabbcaabbccacacbabccacaababcbb"
words6 = ["c","b","a","c","a","a","a","b","c"]
output6 = [6,16,17,18,19,20]

str7 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
words7 = ["aa", "aa", "aa"]
output7 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

'''
str4 = "tomatotomatotom"
words4 = ["tomato", "tom"]
output4 = [0, 6]

Not a valid example because "It is given that all words are of the same length."
'''

strs = [str1, str2, str3, str4, str5, str6, str7]
patterns = [words1, words2, words3, words4, words5, words6, words7]
expected_outputs = [output1, output2, output3, output4, output5, output6, output7]

# My Solution ---------------------------------------------------------------------------
'''
Time Complexity
The time complexity of the algorithm will be O(K + M * N) where 'M' is the length of each word in words, 'N' is the length of string s, and 'K' is the number of words in words

Space Complexity #
The space complexity of the algorithm is O(K) since in the worst case, words can have distinct words which will go into the HashMap. In the worst case, we also need O(N) space for the resulting substring, which will happen when every character in s is a valid contatenation.
'''

import collections
def find_word_contatenation(s, words):
    res = []
    words_count = collections.Counter(words)
    word_len = len(words[0])
    substr_len = word_len * len(words)

    # the start of the substring can be shifted 
    '''
    For example, if we have words = ["foo", "bar"], then starting from index 3 is pointless since by starting at index 0, we will move over index 3. However, we will still need to try starting from indices 1 and 2, in case the input looks something like s = "xfoobar" or s = "xyfoobar". As such, we will only need to perform the sliding window wordLength amount of times.
    '''
    for window_start in range(word_len):
        seen = collections.defaultdict(int)
        matched = 0
        for word_start in range(window_start, len(s), word_len):
            word = s[word_start:word_start + word_len]
            if word not in words_count:
                # found a word that should not be in the substring - reset the window
                window_start = word_start + word_len
                seen = collections.defaultdict(int)
                matched = 0
            else:
                seen[word] += 1
                if seen[word] == words_count[word]:
                    matched += 1
                # shrink the windoe by moving the window_start to the right
                while word_start - window_start + word_len > substr_len or seen[word] > words_count[word]:
                    left_word = s[window_start:window_start + word_len]
                    if seen[left_word] == words_count[left_word]:
                        matched -= 1
                    seen[left_word] -= 1
                    window_start += word_len
                if matched == len(words_count):
                    res.append(window_start)
    return res
        
# Tests
def test_my_solution():
    for i in range(len(strs)):
        output = find_word_contatenation(strs[i], patterns[i])
        assert sorted(output) == expected_outputs[i], "Test" + str(i + 1) + " Output: " + str(
            output) + " str " + strs[i] + " pattern: " + str(patterns[i]) + " should return " + str(expected_outputs[i])
    print("My Solution: ALL TESTS PASSED!")

test_my_solution()


