# day 124
# cs50 + two sum review + add two numbers
# ill be using hash maps for two sum
# brute force -> nestedloops -> O(n^2)
# hash map -> O(n) time and O(n) space
nums = [2, 7, 11, 15]
target = 9


def twosum(nums, target):
    for i in range(len(nums)):  # loop through the list
        for j in range(i + 1, len(nums)):  # loop through the list starting from the next index
            # check if the sum of the two numbers is equal to the target
            if nums[i] + nums[j] == target:
                return [i, j]


def twosum_hash(nums, target):
    hash_map = {}  # create a hash map to store the numbers and their indices
    for i in range(len(nums)):  # loop through the list
        # calculate the complement of the current number
        complement = target - nums[i]
        if complement in hash_map:  # check if the complement is in the hash map
            # return the indices of the two numbers
            return [hash_map[complement], i]
        # add the current number and its index to the hash map
        hash_map[nums[i]] = i

# lets try  Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class ListNode:
    # initialize the ListNode with a value and a reference to the next node
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    # create a dummy node to serve as the head of the result linked list
    dummy = ListNode(0)
    current = dummy  # create a pointer to the current node in the result linked list
    carry = 0  # initialize a variable to keep track of the carry from the previous addition

    while l1 or l2 or carry:  # loop until both linked lists are fully traversed and there is no carry left
        # get the value of the current node in the first linked list, or 0 if the linked list is fully traversed
        val1 = l1.val if l1 else 0
        # get the value of the current node in the second linked list, or 0 if the linked list is fully traversed
        val2 = l2.val if l2 else 0

        # calculate the total sum of the current digits and the carry from the previous addition
        total = val1 + val2 + carry

        # calculate the digit to be stored in the current node of the result linked list (the last digit of the total)
        digit = total % 10
        # calculate the new carry for the next addition (the remaining digits of the total)
        carry = total // 10

        # create a new node with the calculated digit and link it to the current node in the result linked list
        current.next = ListNode(digit)
        # move the current pointer to the next node in the result linked list
        current = current.next

        if l1:  # move the pointer of the first linked list to the next node if it exists
            l1 = l1.next  # move the pointer of the first linked list to the next node if it exists
        if l2:  # move the pointer of the second linked list to the next node if it exists
            l2 = l2.next  # move the pointer of the second linked list to the next node if it exists

    # return the head of the result linked list (the next node of the dummy node)
    return dummy.next
