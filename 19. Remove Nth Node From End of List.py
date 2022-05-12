from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_nodes(nodes: List[int]):
    head = ListNode(nodes[0])
    pointer = head
    for val in nodes[1:]:
        pointer.next = ListNode(val)
        pointer = pointer.next
    return head


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    tmp_node = ListNode(next=head)

    left_pointer = tmp_node
    right_pointer = tmp_node

    for i in range(n):
        right_pointer = right_pointer.next

    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    left_pointer.next = left_pointer.next.next
    return tmp_node.next


if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5]
    list_node = create_linked_nodes(nodes)

    res = removeNthFromEnd(list_node, 5)
    print(res)