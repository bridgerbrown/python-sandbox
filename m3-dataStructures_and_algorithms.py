# %%
# append list method
num_list = []
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)
# %%
# insert list method
num_list = [1, 2, 3, 4, 5]
num_list.insert(3, 4)
print(num_list)
# %%
# pop list method
houses = ["red", "blue", "green"]
last_house = houses.pop()
print(last_house)
print(houses)
# %%
# remove list method
numbers = [1, 2, 3, 4, 5]
numbers.remove(4)
print(numbers)
# %%
# list slicing
numbers = [1, 2, 3, 4, 5]
print(numbers[2:5])
# %%
# in operator
colors = ["green", "red", "blue"]
print("blue" in colors)
# %%
# List Comprehension
nums = [1, 2, 3, 4, 5]
nums_double = []

for n in nums:
    nums_double.append(n * 2)

print(nums)
print(nums_double)
# %%
# with condition
nums = [1, 2, 3, 4]
nums_double = [n * 2 for n in nums if n % 4 == 0]

print(nums)
print(nums_double)
# %%
# multiple lists with comprehension
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)
# %%
# Tuples
car = ("Ford", "Raptor", 2019, "Red")
print(car)
print(car[1])
# %%
# Dictionary data structure
empty_dict = {}
print(empty_dict)

phone_book = {"Bat": 7474, "Cer": 7373, "Cho": 7272}
print(phone_book)
# %%
# dict() constructor
empty_dict = dict()
print(empty_dict)

phone_book = dict(Batman=12345, Cersei=23456, Ghosts=34567)
print(phone_book)
phone_book.get("Batman")
# %%
# Adding/Updating Dict Entries
phone = {"bat": 123}
print(phone)

phone["bat"] = 321
print(phone)
# %%
# Deleting Dict Entries
phone = {"bat": 1}
print(phone)

del phone["bat"]
print(phone)
# %%
# Copying Dict Contents
phone = {"bat": 1}
phone2 = {"you": 2}
print(phone)

phone.update(phone2)
print(phone)
# %%
# Dictionary Comprehension
houses = {1: "Gryf", 2: "Slyth", 3: "Huffle"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)
# %%
# Sets
random_set = {"Yo", 1234, (True, False)}
print(random_set)
print(len(random_set))

empty_set = set()
print(empty_set)
# %%
# Updating a set
empty_set = set()
empty_set.add(1)
empty_set.update([2, 3, 4])
print(empty_set)
# %%
# Set unions
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c'}

print(set_A | set_B)
print(set_A.union(set_B))
# %%
# Set Intersection
set_A = {1, 2, 3, 4}
set_B = {2, 3, 5}

print(set_A & set_B)
print(set_A.intersection(set_B))
# %%
# Set Difference
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 15}

print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))

# %%
# Exercise: List to Tuple
my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
my_tuple = (my_list[0], my_list[-1], len(my_list))
print(my_tuple)
# %%
# Exercise: Kth Maximum Integer in a List
test_list = [1, 5, 8, 3]
k = 2
test_list.sort()
kth_max = test_list[len(test_list) - k]
print(kth_max)
# %%
# Exercise: Highs and Lows
num_list = [20, 9, 51, 81, 50, 42, 77]

def count_low_high(num_list):
    if (len(num_list) == 0):
        return None
    high = list(filter(lambda n: n > 50 or n % 3 == 0, num_list))
    low = list(filter(lambda n: n <= 50 and not n % 3 == 0, num_list))
    return [len(low), len(high)]

print(count_low_high(num_list))
# %%
# Stacks
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items
    
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False
    
def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False
    
print(is_paren_balanced("(((({}))))"))
print(is_paren_balanced("(((({})))"))
# %%
# Reversing a string in a stack
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items
    
def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    
    return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))
# %%
# Exercise: Convert Decimal Integer to Binary
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items
    
def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0
    
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
    
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    
    return bin_num

print(convert_int_to_bin(56))
# %%
# Singly Linked Lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node doesnt exist.")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
            
            prev = None
            count = 0
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return
            
            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")

llist.prepend("D")

llist.delete_node("B")
llist.delete_node("E")
llist.delete_node_at_pos(0)

llist.print_list()
print(llist.len_iterative())
print(llist.len_recursive(llist.head))
# %%
