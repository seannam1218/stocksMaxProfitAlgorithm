import math

def findMaxProfit(arr):
    if len(arr) < 2:
        return "error"
    maxProfit = -math.inf
    max = arr[0]
    min = arr[0]
    prev = math.inf
    for item in arr:
        if item > max:
            max = item
            if max-min > maxProfit:
                maxProfit = max - min
        if item < min:
            min = item
            max = item
            if item - prev > maxProfit:
                maxProfit = item-prev

        prev = item
    return maxProfit

print(findMaxProfit([1,2,5]))
print(findMaxProfit([5,2,1,-3]))
print(findMaxProfit([5,2,10]))
print(findMaxProfit([9,10,3,8,1,2]))
