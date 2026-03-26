from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


# ---- Forward List ----
print("---- Build a forward list ----")
lst = SinglyLinkedList()
lst.build_list_forward([10, 20, 30, 40, 50])
lst.display()

print("Delete the first node:")
lst.delete_first()
lst.display()

print("Delete the last node:")
lst.delete_last()
lst.display()

print("Delete the interior node (30):")
lst.delete_value(30)
lst.display()


# ---- Backward List ----
print("\n---- Build a backward list ----")
lst2 = SinglyLinkedList()
lst2.build_list_backward([10, 20, 30, 40, 50])
lst2.display()

print("Delete the first node:")
lst2.delete_first()
lst2.display()

print("Delete the last node:")
lst2.delete_last()
lst2.display()

print("Delete the interior node (30):")
lst2.delete_value(30)
lst2.display()


# ---- Reverse Display ----
print("\n---- Non-recursive reverse print test ----")
lst3 = SinglyLinkedList()
lst3.build_list_forward([10, 20, 30, 40, 50])
lst3.display()
lst3.display_reverse_nr()


# ---- Remove All ----
print("\n---- Remove all test ----")
lst4 = SinglyLinkedList()
lst4.build_list_forward([1, 2, 4, 6, 1, 3, 6])
lst4.display()

print("Removing 1:")
lst4.remove_all(1)
lst4.display()

print("Removing 6:")
lst4.remove_all(6)
lst4.display()


# ---- Split Evens Odds ----
print("\n---- Split Evens and Odds ----")
split_list = SplitEvensOdds()
split_list.build_list_forward([1,2,3,4,5,6,7,8,15,14,13,12,11,10,9])

split_list.display()

evens, odds = split_list.split_even_odd()

print("Evens list:")
evens.display()

print("Odds list:")
odds.display()

print("Original list (should be empty):")
split_list.display()