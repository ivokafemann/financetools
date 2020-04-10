import matplotlib.pyplot as plt

"""
A small tool to calculate the value of an investment at different interest rates in the future.

Asks the user how much money, over which time horizon and at what interest rates he wants to invest.

Args:
    (int) P - value of initial investment
    (int) r - interest rates
    (int) t - time in years
Returns:
    (int) Pt - Value of investment in the future after t years
"""
P = int(input('\nHow much money would you like to invest?\n'))
r = str(input('\nEnter any number of interest rates you would like to compare (seperated by space, only integers):\n'))
t = int(input('\nWhat is the time horizon in years for the investment?\n'))

rL = [int(i) for i in r.split()]
tL = list(range(t+1))

#Compound Interest Function
def compound_interest(P,r,t):
    Pt = P * (1 + r/100)**t
    return Pt
