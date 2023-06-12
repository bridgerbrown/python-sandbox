# Array Advance Game
def arary_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx

# Arbitrary Precision Increment
A1 = [1, 4, 9]
A2 = [9, 9, 9]

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.appen(0)
    return A

print(plus_one(A1))
print(plus_one(A2))

# Two Sum Problem

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def two_sum_brute_force(A, target):
        for i in range(len(A) - 1):
            for j in range(i+1, len(A)):
                if A[i] + A[j] == target:
                    print(A[i], A[j])
                    return True
        return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def two_sum_hash_table(A, target):
        ht = dict()
        for i in range(len(A)):
            if A[i] in ht:
                print(ht[A[i]], A[i])
                return True
            else:
                ht[target - A[i]] = A[i]
        return False

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def two_sum(A, target):
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
            elif A[i] + A[j] < target:
                i += 1
            else:
                j -= 1
        return False

# Optimal Task Assignment
A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])

# Intersection of Two Sorted Arrays
A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

    # slower, but works if not sorted
    print(set(A).intersection(B))

    # if sorted
    def intersect_sorted_array(A, B):
        i = 0
        j = 0
        intersection = []

        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                if i == 0 or A[i] != A[i - 1]:
                    intersection.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return intersection

    print(intersect_sorted_array(A, B))

# Exercise: Buy and Sell Stock
def buy_and_sell_stock_once(prices):
    max_profit = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit

# More efficient solution
def buy_and_sell_stock_once(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_prices
        max_profit = max(max_profit, compare_profit)
    return max_profit
