def bestTime(prices):
    lowest=float('inf')
    best=0
    for price in prices:
        best=max(best,price-lowest)
        lowest=min(lowest,price)
    return f"Best_Price: {best}, Lowest_price: {lowest}"

print(bestTime([7,1,5,8,9]))