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