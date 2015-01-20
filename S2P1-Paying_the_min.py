balance=float(balance)
annualInterestRate=float(annualInterestRate)
monthlyPaymentRate=float(monthlyPaymentRate)

suma=0.0

for i in range(1,13):
    print("Month: "+str(i))
    print("Minimum monthly payment: 
"+str(round(balance*(monthlyPaymentRate),2)))
    suma+=balance*monthlyPaymentRate
    balance-=balance*monthlyPaymentRate
    balance+=balance*(annualInterestRate/12)
    print("Remaining balance: "+str(round(balance,2)))
print("Total paid: "+str(round(suma,2)))
print("Remaining balance: "+str(round(balance,2)))
