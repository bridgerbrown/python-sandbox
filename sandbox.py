def print_function():
    print("hello")

print_function()


def multiply_by_10(n):
    n *= 10
    num = n
    return n


# format() method
# %%
string1 = "Hello {person}".format(person = "Scoobert")
print(string1)


# %%
# Lambdas
triple = lambda num : num * 3
print(triple(10))

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]
print(concat_strings("World", "Wide", "Web"))

my_func = lambda num: "High" if num > 50 else "Low"
print(my_func(60))

def calculator(operation, n1, n2):
    return operation(n1, n2)

result = calculator(lambda n1, n2: n1 * n2, 10, 20)
print(result)

# %%
# Functions as arguments
num_list = [0, 1, 2]
double_list = map(lambda n: n * 2, num_list)
print(list(double_list))

greater_than_1 = list(filter(lambda n: n > 1, num_list))
print(greater_than_1)
# %%
# Recursion
def rec_count(number):
    print(number)
    if number == 0:
        return 0
    rec_count(number - 1)
    print(number)
rec_count(5)
# %%
def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return -1
    return n * factorial(n - 1)
print(factorial(5))
# %%
# Loops
for i in range(1, 11, 3):
    print(i)

n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
    for n2 in num_list:
        if(n1 != n2):
            if(n1 + n2 == n):
                print(n1, n2)

def check_sum(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False
print(check_sum([10, -14, 26, 5, -3, 13, -5]))
# %%
