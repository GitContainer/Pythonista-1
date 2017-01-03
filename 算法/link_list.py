class LinkNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def init(n):
    return LinkNode(n)


def insert(head, index, linknode):
    if isinstance(head, LinkNode):
        temp = head
        for _ in range(index - 1):
            temp = temp.next
        if temp.next is not None:
            linknode.next = temp.next
        temp.next = linknode


def delete(head, index):
    if isinstance(head, LinkNode):
        temp = head
        for _ in range(index - 1):
            temp = temp.next
        if temp.next is not None:
            temp.next = temp.next.next
        temp.next = None


def printList(head):
    temp = head

    while temp.next is not None:
        print(temp.value, end=' ')
        temp = temp.next


l = init(1)
for _ in range(10):
    insert(l, _, LinkNode((_ + 1)*2))
printList(l)
