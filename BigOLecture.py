count = 0
def my_print_counter(thing_to_print):
    global count
    count += 1
    print(thing_to_print)

my_items = [1,2,3,4,5]

"""
O(1) - Constant Time
"""
# def print_first_item(items):
#     my_print_counter(items[0])

# print_first_item(my_items)



"""
O(n) - Linear Time
"""
# def print_all_items(items):
#     for item in items:
#         my_print_counter(item)

# print_all_items(my_items)



"""
O(n^2) - Quadratic Time
"""
# def print_all_possible_ordered_pairs(items):
#     for first_item in items:
#         for second_item in items:
#             my_print_counter((first_item, second_item))

# print_all_possible_ordered_pairs(my_items)



"""
N could be the actual input, or the size of the input
"""
# def say_hi_n_times(n):
#     for time in range(n):
#         my_print_counter("hi")

# say_hi_n_times(10)


# def print_all_items(items):
#     for item in items:
#         my_print_counter(item)

# print_all_items(my_items)



"""
Drop the constants
"""
# O(2n) is simplified to what?
# def print_all_items_twice(items):
#     for item in items:
#         my_print_counter(item)

#     # Once more, with feeling
#     for item in items:
#         my_print_counter(item)

# print_all_items_twice(my_items)


# O(1 + n/2 + 100) is simplified to what?
# def print_first_item_then_first_half_then_say_hi_100_times(items):
#     my_print_counter(items[0]) # O(1)

#     middle_index = len(items) / 2
#     index = 0
#     while index < middle_index: # O(n/2)
#         my_print_counter(items[index])
#         index += 1

#     for time in range(100): # O(100)
#         my_print_counter("hi")

# print_first_item_then_first_half_then_say_hi_100_times(my_items)



"""
Drop the less significant terms
"""
# O(n + n^2) is simplified to what?
# def print_all_numbers_then_all_pair_sums(numbers):
#     print("these are the numbers:")
#     for number in numbers: # O(n)
#         my_print_counter(number)

#     print("and these are their sums:")
#     for first_number in numbers: # O(n^2)
#         for second_number in numbers:
#             my_print_counter(first_number + second_number)

# print_all_numbers_then_all_pair_sums(my_items)



"""
We are usually talking about the "worst case"
"""
# my_haystack = [1,2,3,4,5,6,7,8,9,10]
# def contains(haystack, needle):

#     # Does the haystack contain the needle?
#     for item in haystack:
#         if item == needle:
#             return True

#     return False

# contains(my_haystack, 1)



"""
Things to remember with Big O
"""
# 1. sometimes constants matter (even though we can drop them in Big O)
# 2. beware of premature optimization


"""
Show DESMOS graph before the break
https://www.desmos.com/calculator
"""

# Linked Lists

# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node
    
#     def get_value(self):
#         return self.value

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next

# class LinkedList:
#     def __init__(self, head, tail):
#         self.head = None
#         self.tail = None
    
#     # append
#     def add_to_tail(self, value):
#         new_node = Node(value, None)
#         # check if there is no head
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node
    
#     def remove_head(self):
#         # is there a head?
#         if not self.head:
#             return None
        
#         # if head has no next value (1 item in list)
#         if not self.head.get_next():
#             head = self.head
#             self.head = None
#             self.tail = None

#             return head.get_value()

#         value = self.head.get_value()
#         # set the head reference to the current head's next node in the list
#         self.head = self.head.get_next()
#         return value

#     def contains(self, value):
#         if not self.head:
#             return False
#     # get a reference to the node we're currently at; update this as we travers the list
#     current = self.head
#     # check to see if we're at a valid node
#     while current:
#         # return True if the current value we're looking at matches our target value
#         if current.get_value() == value:
#             return True
#         current = 
            