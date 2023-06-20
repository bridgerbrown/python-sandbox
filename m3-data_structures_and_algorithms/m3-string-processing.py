# String Processing

# Look-and-Say Sequence
def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

# Spreadsheet Encoding
def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str)-1
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1
    return num

# Is Palindrome
s = "Was it a cat I saw?"

    # Solution uses extra space
    s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
    print(s == s[::1])

    # Preferred Solution
def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

# Is Anagram
s1 = "fairy tales"
s2 = "rail safety"
    # O(logn)
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()
print(sorted(s1) == sorted(s2))

    # Linear time complexity
def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True

# Is Palindrome Permutation
def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

# Check Permutation

    # Time: O(n log n), Space: O(1)
def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False
    
    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)

    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    return True

    # Time: O(n), Space: O(n)
def is_perm_2(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    d = dict()

    for i in str_1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            return False

    return all(value == 0 for value in d.values())

# Exercise: Is Unique
def is_unique(input_str):
    input_str = input_str.lower()
    
    d = dict()

    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

# Integer to String
def int_to_str(input_str):

    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []

    if input_str == 0:
        output_str.append('0')
    else:
        while input_int > 0:
            output_str.append(chr(ord('0') + input_int % 10))
            input_int //= 10
        output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str

# Exercise: String to Integer
def str_to_int(input_str):

    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i] - ord('0'))
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    else:
        return output_int
