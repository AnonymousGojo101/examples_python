"""
Problem 2000: Reverse Prefix of Word

Given a 0-indexed string word and a character ch, reverse the segment of word 
that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). 
If the character ch does not exist in word, do nothing.

Return the resulting string.

Constraints:
- 1 <= word.length <= 250
- word consists of lowercase English letters.
- ch is a lowercase English letter.

Examples:

Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: Reverse the part of word from index 0 to 3, inclusive.

Example 2:
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"

Example 3:
Input: word = "abcd", ch = "z"
Output: "abcd"
"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    word1 = "abcdefd"
    ch1 = "d"
    expected1 = "dcbaefd"
    result1 = sol.reversePrefix(word1, ch1)
    print("Test case 1:")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    word2 = "xyxzxe"
    ch2 = "z"
    expected2 = "zxyxxe"
    result2 = sol.reversePrefix(word2, ch2)
    print("Test case 2:")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    word3 = "abcd"
    ch3 = "z"
    expected3 = "abcd"
    result3 = sol.reversePrefix(word3, ch3)
    print("Test case 3:")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
