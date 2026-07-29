##ARRAY


arr = [12,45,89,23,67,3,8,33]

#1
print("Array elements :")
for num in arr:
    print(num)

# Time Complexity: O(n)
# Space Complexity: O(1)


#2 (i)

print("Array length :", len(arr))

# Time Complexity: O(1)
# Space Complexity: O(1)

# (ii)

count = 0
for i in range(len(arr)):
    count += 1
print("Array length :", count)    

# Time Complexity:O(n)
# Space Complexity:O(1)


#3

biggest = arr[0]

for num in arr:
    if num > biggest:
        biggest = num
print("Biggest :", biggest)

# Time Complexity:O(n)
# Space Complexity:O(1)

#4

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num
print("Smallest :", smallest)

# Time Complexity:O(n)
# Space Complexity:O(1)

#5

target = 67

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index :", i)
        break
else:
    print(f"{target} not found")

# Time Complexity: O(n)
# Space Complexity: O(1)
