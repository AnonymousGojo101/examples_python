"""
Problem: Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Constraints:
0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        # Initialize an empty linked list with a dummy head node
        self.head = None

    def get(self, index: int) -> int:
        # Return the value of the node at the specified index (if exists)
        pass

    def addAtHead(self, val: int) -> None:
        # Add a node of value val before the first element of the linked list
        pass

    def addAtTail(self, val: int) -> None:
        # Append a node of value val as the last element of the linked list
        pass

    def addAtIndex(self, index: int, val: int) -> None:
        # Add a node of value val before the indexth node in the linked list
        pass

    def deleteAtIndex(self, index: int) -> None:
        # Delete the indexth node in the linked list
        pass


def main():
    # Test the MyLinkedList implementation
    
    myLinkedList = MyLinkedList()
    
    # Test case 1: Add a node at the head, then at the tail, and at index 1
    myLinkedList.addAtHead(1)  # linked list becomes 1
    myLinkedList.addAtTail(3)  # linked list becomes 1 -> 3
    myLinkedList.addAtIndex(1, 2)  # linked list becomes 1 -> 2 -> 3
    print("Test case 1:")
    print(f"Expected list: 1 -> 2 -> 3")
    print(f"Result: {myLinkedList.get(0)} -> {myLinkedList.get(1)} -> {myLinkedList.get(2)}")
    print()

    # Test case 2: Delete the node at index 1
    myLinkedList.deleteAtIndex(1)  # linked list becomes 1 -> 3
    print("Test case 2:")
    print(f"Expected list after deletion: 1 -> 3")
    print(f"Result: {myLinkedList.get(0)} -> {myLinkedList.get(1)}")
    print()

    # Test case 3: Test getting an invalid index
    print("Test case 3:")
    print(f"Expected output: -1")
    print(f"Result: {myLinkedList.get(3)}")
    print()


if __name__ == "__main__":
    main()
