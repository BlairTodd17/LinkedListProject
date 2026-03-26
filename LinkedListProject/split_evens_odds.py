from singly_linked_list import SinglyLinkedList, Node


class SplitEvensOdds(SinglyLinkedList):
    def split_even_odd(self):
        evens = SinglyLinkedList()
        odds = SinglyLinkedList()

        current = self.head

        while current:
            next_node = current.next
            current.next = None

            if current.data % 2 == 0:
                if evens.head is None:
                    evens.head = current
                else:
                    temp = evens.head
                    while temp.next:
                        temp = temp.next
                    temp.next = current
            else:
                if odds.head is None:
                    odds.head = current
                else:
                    temp = odds.head
                    while temp.next:
                        temp = temp.next
                    temp.next = current

            current = next_node

        self.head = None

        return evens, odds