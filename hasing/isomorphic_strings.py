"""
Problem: Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Constraints:
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ASCII character.

Examples:

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation: The strings s and t can be made identical by:
    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation: The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    s1 = "egg"
    t1 = "add"
    expected1 = True
    result1 = sol.isIsomorphic(s1, t1)
    print("Test case 1: s =", s1, ", t =", t1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    s2 = "foo"
    t2 = "bar"
    expected2 = False
    result2 = sol.isIsomorphic(s2, t2)
    print("Test case 2: s =", s2, ", t =", t2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    s3 = "paper"
    t3 = "title"
    expected3 = True
    result3 = sol.isIsomorphic(s3, t3)
    print("Test case 3: s =", s3, ", t =", t3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
