balance=5000
def buy_all_things(item,price):
    global balance
    print(f"Global Balance {balance}")
    balance= balance-price
    print(f"Balance after buy {balance}")

buy_all_things('T-shart',2000)
print(balance)