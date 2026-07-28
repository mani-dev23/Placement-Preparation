###Practice Questions

#1 
n =100
for i in range(n):
    print(i)

for j in range(n):
    print(j)

# Time Complexity O(2n) --> O(n)

#2

i = n

while i > 1:
    i = i // 2

# Time Complexity O(log n)

#3

for i in range(n):
    for j in range(10):
        print(i, j)

# Time Complexity O(n)

#4

for i in range(100):
    print(i)

# Time Complexity O(1)

#5

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)

# Time Complexity O(n**3)

###HOME_WORK

#1

for i in range(50):
    print(i)

# Time Complexity O(1)
# Space Complexity O(1)

#2

n = 64

while n > 1:
    print(n)
    n //= 2

# Time Complexity O(log n)
# Space Complexity O(1)



#3

for i in range(10):
    for j in range(10):
        print(i, j)

# Time Complexity O(1)
# Space Complexity O(1)

#4

for i in range(100):
    print(i)

for j in range(100):
    print(j)

# Time Complexity O(1)
# Space Complexity O(1)   

#5

for i in range(n):
    print(i)

# It have Time Complexity O(n) because it has one loop. It has n number of inputs so the output is linear to the input so, it has O(n) 