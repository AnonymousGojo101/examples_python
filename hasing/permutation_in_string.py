"""
Problem: Permutation in String

Given two strings `s1` and `s2`, return true if `s2` contains a permutation of `s1`, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.

Examples:

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    s1_1 = "ab"
    s2_1 = "eidbaooo"
    expected1 = True
    result1 = sol.checkInclusion(s1_1, s2_1)
    print("Test case 1: s1 =", s1_1, ", s2 =", s2_1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    s1_2 = "ab"
    s2_2 = "eidboaoo"
    expected2 = False
    result2 = sol.checkInclusion(s1_2, s2_2)
    print("Test case 2: s1 =", s1_2, ", s2 =", s2_2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
