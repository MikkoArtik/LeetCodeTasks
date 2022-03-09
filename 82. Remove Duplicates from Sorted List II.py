# Task: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self,
                         head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        bad_nums = set()
        node = head
        new_head, tail = None, None
        while node:
            val = node.val
            if val in bad_nums:
                node = node.next
            else:
                next_node = node.next
                if next_node:
                    if next_node.val == node.val:
                        bad_nums.add(node.val)
                        node = node.next
                    else:
                        add_node = ListNode(node.val)
                        if not new_head:
                            new_head = add_node
                            tail = new_head
                        else:
                            tail.next = add_node
                            tail = add_node
                else:
                    add_node = ListNode(node.val)
                    if not new_head:
                        new_head = add_node
                        tail = new_head
                    else:
                        tail.next = add_node
                        tail = add_node

                node = node.next
        return new_head
