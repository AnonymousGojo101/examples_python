"""
Problem 1496: Path Crossing

You are given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north,
south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited.
Return false otherwise.

Examples:

Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

Constraints:
- 1 <= path.length <= 10^4
- path[i] is either 'N', 'S', 'E', or 'W'.
"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Set to track the positions we have visited
        visited_positions = set()
        
        # Start at the origin (0, 0)
        x, y = 0, 0
        
        # Add the origin to the visited set
        visited_positions.add((x, y))
        
        # Move along the path
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
                
            # If we have already visited the new position, return True
            if (x, y) in visited_positions:
                return True
            
            # Add the new position to the visited set
            visited_positions.add((x, y))
        
        # If no crossing, return False
        return False


def main():
    sol = Solution()

    # Test case 1
    path1 = "NES"
    expected1 = False
    result1 = sol.isPathCrossing(path1)
    print("Test case 1:", result1)
    assert result1 == expected1, f"Failed: expected {expected1}, got {result1}"
    print("Passed ✅\n")

    # Test case 2
    path2 = "NESWW"
    expected2 = True
    result2 = sol.isPathCrossing(path2)
    print("Test case 2:", result2)
    assert result2 == expected2, f"Failed: expected {expected2}, got {result2}"
    print("Passed ✅\n")


if __name__ == "__main__":
    main()
