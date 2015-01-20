def test(x):
    in_balance = balance
    for s in range(1, 13):
        in_balance -= x
        in_balance += in_balance * (annualInterestRate / 12)
    return round(in_balance, 2)

endval = 0
balance = float(balance)
annualInterestRate = float(annualInterestRate)

for i in range(10, int(balance), 10):
    if test(i) <= 0:
        endval = i
        break
print ("Lowest Payment: " + str(endval))
