"""
Problem 1456: Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters 
in any substring of s with length k.

Vowels: 'a', 'e', 'i', 'o', 'u'

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length

Examples:

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowels.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: Substrings "lee", "eet", and "ode" all contain 2 vowels.
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    s1 = "abciiidef"
    k1 = 3
    expected1 = 3
    result1 = sol.maxVowels(s1, k1)
    print("Test case 1:")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    s2 = "aeiou"
    k2 = 2
    expected2 = 2
    result2 = sol.maxVowels(s2, k2)
    print("Test case 2:")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    s3 = "leetcode"
    k3 = 3
    expected3 = 2
    result3 = sol.maxVowels(s3, k3)
    print("Test case 3:")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
