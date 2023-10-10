# Fruits into Baskets
# Sliding Window - Medium

'''
Problem Statement #
Given an array of characters where each character represents a fruit tree, you
are given two baskets and your goal is to put maximum number of fruits in each
basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree.
You will pick one fruit from each tree until you cannot, i.e., you will stop
when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

My Examples
-----------
Example 3:
Input: Fruit=['A', 'B', 'C', 'B', 'A', 'B', 'C', 'B', 'C', 'A']
Output: 4
'''

# My Solution
# Similar to Longest Substring with K Distinct Characters, but now we have a fixed K = 2
# When shrinking the sliding window, we will update the start of the window to be
# the right of the fruit tree with the earliest last occurence.

# Time Complexity: O(N) - del_fruit_with_earliest_last_occurance() is O(1)
# Space Complexity: O(1)

def fruit_into_basket(fruits):
    max_num = 0
    start = 0
    # Hashmap to keep track of the fruits and their last seen index in the sliding window
    fruit_map = {}

    def del_fruit_with_earliest_last_occurance():
        index = len(fruits)
        fruit_to_remove = None
        for fruit in fruit_map:
            if fruit_map[fruit] < index:
                index = fruit_map[fruit]
                fruit_to_remove = fruit
        del fruit_map[fruit_to_remove]
        return index

    for end in range(len(fruits)):
        fruit_map[fruits[end]] = end
        if len(fruit_map) > 2:
            start = del_fruit_with_earliest_last_occurance() + 1
        max_num = max(max_num, end - start + 1)
    return max_num

# Tests            
fruits1 = ['A', 'B', 'C', 'A', 'C']
ans1 = fruit_into_basket(fruits1)
expected_ans1 = 3
assert ans1 == expected_ans1, "Output: " + str(ans1) + " fruits " + fruits1 + " should return " + str(expected_ans1)

fruits2 = ['A', 'B', 'C', 'B', 'B', 'C']
ans2 = fruit_into_basket(fruits2)
expected_ans2 = 5
assert ans2 == expected_ans2, "Output: " + str(ans2) + " fruits " + fruits2 + " should return " + str(expected_ans2)

fruits3 = ['A', 'B', 'C', 'B', 'A', 'B', 'C', 'B', 'C', 'A']
ans3 = fruit_into_basket(fruits3)
expected_ans3 = 4
assert ans3 == expected_ans3, "Output: " + str(ans3) + " fruits " + fruits3 + " should return " + str(expected_ans3)
print("My Solution: ALL TESTS PASSED!")

# Educative.io Solution
'''
This problem follows the Sliding Window pattern and is quite similar to Longest Substring with K Distinct Characters. In this problem, we need to find the length of the longest subarray with no more than two distinct characters (or fruit types!). This transforms the current problem into Longest Substring with K Distinct Characters where K=2.

Time Complexity:
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input array. The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).

Space Complexity:
The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the frequency map.
'''

def fruits_into_baskets_educative(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            window_start += 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

# Tests
def test_educative_solution():
    fruits_inputs = [fruits1, fruits2, fruits3]
    expected_outputs = [expected_ans1, expected_ans2, expected_ans3]
    for i in range(len(fruits_inputs)):
        ans = fruits_into_baskets_educative(fruits_inputs[i])
        assert ans == expected_outputs[i], "Output: " + str(ans) + " fruits " + fruits_inputs[i] + " should return " + str(expected_outputs[i])
    print("Educative.io Solution: ALL TESTS PASSED!")
test_educative_solution()
