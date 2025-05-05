"""
Problem 557: Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order.

Constraints:
- 1 <= s.length <= 5 * 10^4
- s contains printable ASCII characters.
- s does not contain any leading or trailing spaces.
- All the words in s are separated by a single space.
- There is at least one word in s.

Examples:

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # TODO: Implement this method
        pass


def main():
    sol = Solution()
    
    # Test case 1
    s1 = "Let's take LeetCode contest"
    expected1 = "s'teL ekat edoCteeL tsetnoc"
    result1 = sol.reverseWords(s1)
    print("Test case 1:")
    print("Input:", s1)
    print("Output:", result1)
    assert result1 == expected1, f"Failed test case 1: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    s2 = "Mr Ding"
    expected2 = "rM gniD"
    result2 = sol.reverseWords(s2)
    print("Test case 2:")
    print("Input:", s2)
    print("Output:", result2)
    assert result2 == expected2, f"Failed test case 2: expected {expected2}, got {result2}"
    print("Passed ✅\n")

    # Test case 3
    s3 = "a b c"
    expected3 = "a b c"
    result3 = sol.reverseWords(s3)
    print("Test case 3:")
    print("Input:", s3)
    print("Output:", result3)
    assert result3 == expected3, f"Failed test case 3: expected {expected3}, got {result3}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
