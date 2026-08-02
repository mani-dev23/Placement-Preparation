# 1. Array Insertion

arr = [10, 20, 40, 50]

arr.insert(2, 30)
print(arr)

arr.append(80)
print(arr)

# Time Complexity O(n)



# 2. Array Deletion

arr.remove(20)
print(arr)
arr.pop(4)
print(arr)

# Time Complexity O(n)


# 3. Reverse an Array (Method 1)

arr = [10, 20, 30, 40, 50]

arr.reverse()
print(arr)

# Time Complexity O(n)


# 4. Reverse an Array (Without Built-in)


arr = [10, 20, 30, 40, 50]

l = 0
r = len(arr) - 1

while l < r:

    arr[l], arr[r] = arr[r], arr[l]

    l += 1
    r -= 1

print(arr)

# Time Complexity O(n)


# 5. Array Update

arr[3] = 100
print(arr)
# arr(20) = 1000
# print(arr) WRONG



#Home Work

#1  Insert 25 into at index 2.

arr = [10,20,30,40]

arr.insert(2, 25)

print(arr)

# Time Complexity O(1)


#2 Delete 30 from

arr = [10,20,30,40,50]

arr.remove(30)
print(arr)
# Time Complexity O(1)

# 3 Reverse an array without using reverse().

arr = [10, 20, 30, 40, 50, 60, 70, 80]

l = 0
r = len(arr) - 1
while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
print(arr)

# Time Complexity O(n)

#4 Update the third element to 100.

arr[2] = 100
print(arr)

# Time Compleity O(1)