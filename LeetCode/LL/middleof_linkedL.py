#https://leetcode.com/problems/middle-of-the-linked-list/


class Solution(object):
        
    def middleNode(self, head):
        """
        We use hare-tortoise approach // 2 pointers
        By the time fast pointer reaches the end, we will reach the middle.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

#Brute Force
	length = 0
    count = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    if length == 1:
        return head
    
    mid = int(math.floor(length / 2))

    while head:
        count += 1
        head = head.next
        if count == mid:
            return head
        
    return None
