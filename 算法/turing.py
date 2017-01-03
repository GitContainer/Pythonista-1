class Linklist(object):
    def __init__(self, obj):
        self.obj = obj
        self.next = None

    def __str__(self):
        return self.obj


def init():
    return Linklist('HEAD')


def insert(head, index, linklist):
    if isinstance(head, Linklist):
        temp = head
        for i in range(index-1):
            temp = temp.next
        if temp.next is not None:
            linklist.next = temp.next
        temp.next = linklist


def remove(head, index):
    if isinstance(head, Linklist):
        temp = head
        for i in range(index):
            if i == index - 1:
                if temp.next is not None:
                    temp.next = temp.next.next


def print_list(head):
    if isinstance(head, Linklist):
        temp = head
        while temp.next:
            temp = temp.next
            print(temp, end='')


l = init()
insert(l, 1, Linklist('1'))
insert(l, 1, Linklist('2'))
insert(l, 1, Linklist('3'))
insert(l, 1, Linklist('4'))
insert(l, 1, Linklist('5'))
print_list(l)
remove(l, 1)
print()
print_list(l)
