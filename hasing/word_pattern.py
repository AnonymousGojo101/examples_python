"""
Problem: Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Constraints:
- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters.
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '.
- s does not contain any leading or trailing spaces.
- All the words in s are separated by a single space.

Examples:

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation: The bijection can be established as:
    'a' maps to "dog".
    'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    pattern1 = "abba"
    s1 = "dog cat cat dog"
    expected1 = True
    result1 = sol.wordPattern(pattern1, s1)
    print("Test case 1: pattern =", pattern1, ", s =", s1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    pattern2 = "abba"
    s2 = "dog cat cat fish"
    expected2 = False
    result2 = sol.wordPattern(pattern2, s2)
    print("Test case 2: pattern =", pattern2, ", s =", s2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    pattern3 = "aaaa"
    s3 = "dog cat cat dog"
    expected3 = False
    result3 = sol.wordPattern(pattern3, s3)
    print("Test case 3: pattern =", pattern3, ", s =", s3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
