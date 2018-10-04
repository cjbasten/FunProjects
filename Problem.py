# You invest $100.00 today at the rate of 5%. What is the future value of your investment in the following years: 1, 2, 5, 10.

# Formula: FV = PV (1+ i)n

# FV = Future Value
# PV = Present Value
# i = rate of interest
# n = number of compounding periods (years)

PV = 100
i = 0.05
n = input("How many years?")
FV = PV*(1+i)*int(n)
print(FV)

x = [1, 2, 5, 10]
for year in x:
    FV = PV*(1+i)*year
    print(int(FV))