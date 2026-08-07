nums = [0,1,2,2,3,0,4,2]
val = 2

s = len(nums) - 1
f = len(nums) - 1
k = len(nums)

for _ in range (len(nums)):
    if nums[f] == val:
        nums[s], nums[f] = nums[f], nums[s]
        s -= 1
        k -= 1
    f -= 1
print(nums)
print(k)


slow = 0
for fast in range(len(nums)):
    if nums[fast] != val:
        nums[fast], nums[slow] = nums[slow], nums[fast]
        slow +=1

print(nums)
print(slow)

