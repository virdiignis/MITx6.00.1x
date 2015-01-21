def high(x):
    in_balance = x
    for i in range(12):
        in_balance += in_balance * (annualInterestRate / 12.0)
    return in_balance


def test(x):
    in_balance = balance
    for i in range(12):
        in_balance -= x
        in_balance += in_balance * (annualInterestRate / 12.0)
    return round(in_balance, 2)


low = balance / 12.0
higher = high(balance)


while test((low + higher) / 2.0) != 0:
    if test((low + higher) / 2.0) > 0:
        low = (low + higher) / 2.0
    else:
        higher = (low + higher) / 2.0


print("Lowest Payment: " + str(round((low + higher) / 2.0, 2)))
