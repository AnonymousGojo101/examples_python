"""
Problem 1208: Get Equal Substrings Within Budget

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t 
costs |s[i] - t[i]| (absolute difference between ASCII values).

Return the maximum length of a substring of s that can be changed to t with a cost 
less than or equal to maxCost. If no such substring exists, return 0.

Constraints:
- 1 <= s.length <= 10^5
- t.length == s.length
- 0 <= maxCost <= 10^6
- s and t consist of only lowercase English letters.

Examples:

Example 1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" can change to "bcd" with cost 3.

Example 2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Changing each character costs 2, so max substring is length 1.

Example 3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: No changes allowed, so only identical chars count.
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()

    # Test case 1
    s1 = "abcd"
    t1 = "bcdf"
    maxCost1 = 3
    expected1 = 3
    result1 = sol.equalSubstring(s1, t1, maxCost1)
    print("Test case 1:")
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    s2 = "abcd"
    t2 = "cdef"
    maxCost2 = 3
    expected2 = 1
    result2 = sol.equalSubstring(s2, t2, maxCost2)
    print("Test case 2:")
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    s3 = "abcd"
    t3 = "acde"
    maxCost3 = 0
    expected3 = 1
    result3 = sol.equalSubstring(s3, t3, maxCost3)
    print("Test case 3:")
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
