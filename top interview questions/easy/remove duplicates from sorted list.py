class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if not head:
        return None
    buffer = []
    current = head

    while current:
        buffer.append(current.val)
        current = current.next

    result = sorted(list(set(buffer)))

    head = ListNode(result[0])
    current = head

    for value in result[1:]:
        current.next = ListNode(value)
        current = current.next

    return head