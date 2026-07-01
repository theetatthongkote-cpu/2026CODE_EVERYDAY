# Day 155
# rest day
# simple buy stock program

apple_stock_price = 150.0
balance = 1000.0


def buy_stock(stock_price, amount):
    total_cost = stock_price * amount
    return total_cost


def sell_stock(stock_price, amount):
    total_revenue = stock_price * amount
    return total_revenue


# Example usage
amount_to_buy = int(input("Enter the number of Apple shares to buy: "))
cost = buy_stock(apple_stock_price, amount_to_buy)
if cost <= balance:
    balance -= cost
    print(
        f"Bought {amount_to_buy} shares of Apple for ${cost:.2f}. Remaining balance: ${balance:.2f}")
