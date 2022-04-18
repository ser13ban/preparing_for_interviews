from email import header
import pstats
import re
from tkinter.messagebox import NO


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        pass


class LinkedList:
    def __init__(self):
        self.head = None
        self.list_length = -1

    def insert_at_beggining(self, data):
        node = Node(data=data, next=self.head)
        self.head = node
        self.list_length += 1

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
            self.list_length += 1
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
        self.list_length += 1

    def insert_from_list(self, data):
        for item in reversed(data):
            self.insert_at_beggining(item)

    def get_lenght(self):
        return self.list_length

    def delete_first(self):
        self.list_length -= 1
        self.head = self.head.next

    def delete_last(self):
        itr = self.head
        while itr.next.next:
            itr = itr.next

        self.list_length -= 1
        itr.next = None

    def delete_at(self, index):
        if index < 0 or index > self.list_length:
            print("Index is out of bounds!")
            return

        if index == 0:
            self.delete_first()

        if index == self.list_length:
            self.delete_last()

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def removeNthFromEnd(self, head, n: int):
        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head

    def print_list(self):
        if self.head == None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr:
            print(str(itr.data) + " --> ")
            itr = itr.next

    def insert_at(self, index, data):
        if(index < 0 or index > self.list_length):
            print("Index out of bounds, can't insert")
            return

        if index == 0:
            self.insert_at_beggining(data)
            return

        if index == self.list_length:
            self.insert_at_end(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def reverse(self):
        previous = None
        curent = self.head

        while curent:
            following = curent.next
            curent.next = previous
            previous = curent
            curent = following

        self.head = previous

    def delete_by_val(self, val):
        prev = self.head
        itr = self.head.next
        if prev.data == val:
            self.head = self.head.next
            self.list_length -= 1
            return

        while itr:
            if itr.data == val:
                prev.next = prev.next.next
                self.list_length -= 1
            prev = itr
            itr = itr.next


def find_intersecting_ponint(head1, head2):
    nodes = set()
    itr_list1 = head1
    itr_list2 = head2
    while itr_list1 or itr_list2:
        # if itr_list1 and itr_list2 and itr_list1.data == itr_list2.data:
        #     return itr_list1.data
        if itr_list1 == None:
            break

        if itr_list2 == None:
            break

        if itr_list1.data in nodes:
            return itr_list1.data
        else:
            nodes.add(itr_list1.data)

        if itr_list2.data in nodes:
            return itr_list2.data
        else:
            nodes.add(itr_list2.data)

        itr_list2 = itr_list2.next
        itr_list1 = itr_list1.next

    while itr_list1:
        if itr_list1.data in nodes:
            return itr_list1.data
        itr_list1 = itr_list1.next

    while itr_list2:
        if itr_list2.data in nodes:
            return itr_list2.data
        itr_list2 = itr_list2.next

    return None


def main():
    data = [3, 5, 8]
    data2 = [99, 1, 10]
    ll = LinkedList()
    ll.insert_from_list(data)
    ll.print_list()
    print()
    #ll2 = LinkedList()
    # ll2.insert_from_list(data2)
    # ll2.print_list()
    # print(find_intersecting_ponint(ll.head, ll2.head))
    ll.removeNthFromEnd(ll.head, 1)
    ll.print_list()


main()

# TODO reverse Linked list with reccursive function
# TODO Add delete_by val
# TODO Merge to sorted list
# TODO Palindrome linked list
# TODO linked list cycle
