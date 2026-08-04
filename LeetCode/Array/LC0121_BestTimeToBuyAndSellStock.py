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