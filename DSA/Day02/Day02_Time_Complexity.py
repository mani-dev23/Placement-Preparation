"""
=========================================
Day 1 - Time Complexity
Topic: Time & Space Complexity
=========================================
Problems Solved:
1. Print numbers from 1 to n
2. Find largest element
3. Find smallest element
4. Sum of array
5. Count even numbers
=========================================
Name : Manikandan
Day : 2
Date : 27-07-2026
Topic : Time Complexity
=========================================
"""




#1.

n = 10

for i in range(n):
    print(i)

# Time Complexity O(n)
# Space Complexity O(1)


#2.

arr = [10, 13, 5, 23, 3]

largest = arr[0]

for num in arr:
    if largest < num:
        largest = num
print("Largest : ", largest)

# Time Complexity O(n)
# Space Complexity O(1)


#3

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num
print("Smallest : ", smallest)

# Time Complexity O(n)
# Space Complexity O(1)


#4

total = 0

for num in arr:
    total += num
print("Total : ", total)

# Time Complexity O(n)
# Space Complexity O(1)


#5

count = 0
for num in arr:
    if num%2 == 0:
        count +=1
print("Even Count : ",count)

# Time Complexity O(n)
# Space Complexity O(1)