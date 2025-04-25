# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        i = 0
        l = []
        current = head
        while current:
            l.append(current)
            current = current.next
            i += 1

        if n == i:
            return head.next

        l[i - n - 1].next = None if i <= i - n + 1 else  l[i - n + 1]
        return head

sol = Solution()
node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
result = sol.removeNthFromEnd(node, 1)
while result:
    print(result.val)
    result = result.next