"""
Problem: Determine if Two Strings Are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Constraints:
- 1 <= word1.length, word2.length <= 10^5
- word1 and word2 contain only lowercase English letters.

Examples:

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    word1_1 = "abc"
    word2_1 = "bca"
    expected1 = True
    result1 = sol.closeStrings(word1_1, word2_1)
    print("Test case 1: word1 =", word1_1, ", word2 =", word2_1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    word1_2 = "a"
    word2_2 = "aa"
    expected2 = False
    result2 = sol.closeStrings(word1_2, word2_2)
    print("Test case 2: word1 =", word1_2, ", word2 =", word2_2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    word1_3 = "cabbba"
    word2_3 = "abbccc"
    expected3 = True
    result3 = sol.closeStrings(word1_3, word2_3)
    print("Test case 3: word1 =", word1_3, ", word2 =", word2_3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
