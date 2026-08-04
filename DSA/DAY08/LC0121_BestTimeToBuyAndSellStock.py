prices = [7,1,5,3,6,4]


min_price = prices[0]
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit


print("Your Profit ",max_profit)

# Time Complexity O(n)
# Space Complexity O(1)



for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        profit = j - i
        if profit > max_profit:
            max_profit = profit
print(max_profit)

# Time Complexity O(n**2)
# Space Complexity O(1)