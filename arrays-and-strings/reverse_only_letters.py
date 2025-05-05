"""
Problem 917: Reverse Only Letters

Given a string s, reverse the string according to the following rules:
- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

Constraints:
- 1 <= s.length <= 100
- s consists of characters with ASCII values in the range [33, 122].
- s does not contain '\"' or '\\'.

Examples:

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    s1 = "ab-cd"
    expected1 = "dc-ba"
    result1 = sol.reverseOnlyLetters(s1)
    print("Test case 1:")
    print("Input:", s1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    s2 = "a-bC-dEf-ghIj"
    expected2 = "j-Ih-gfE-dCba"
    result2 = sol.reverseOnly
