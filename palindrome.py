class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        #empty array to change from singly linked list to array 
        nums=[]
        #while loop during the length of the singly linked list, as long as the head exists
        while head:
            #val is the variable listed in the class above
            nums.append(head.value)
            head= head.next
        #left and right pointers based on size of array
        left = 0
        right = len(nums) - 1
        #space of left less than or equal to right continue loop
        while left <= right:
            #if value of nums at postion left does not equal value of nums at position right then not a palindrome
            if nums[left] != nums[right]:
                return False
            #continue checking the next value in the index moving towards the center of the array
            left += 1
            right -= 1
        return True    

linked_list = LinkedList()
for val in [1, 2, 2, 1]:
    linked_list.add_node(val)
    
solution = Solution()
result = solution.isPalindrome(linked_list.head)
print(result)

