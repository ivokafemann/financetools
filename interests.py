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
r = str(input('\nEnter interest rates you would like to compare (seperated by space, only integers):\n'))
t = int(input('\nWhat is the time horizon in years for the investment?\n'))

rL = [int(i) for i in r.split()]
tL = list(range(t+1))

#Compound Interest Function
def compound_interest(P,r,t):
    Pt = P * (1 + r/100)**t
    return Pt

#Compound Interest List function:
#Create a list containing n list(s) corresponding to the given interest rate,
#displaying the growth of the principal sum over the given time horizon.
def compound_interests_L(rL,P,tL):
    PL = []
    for r in rL:
        PL.append([compound_interest(P,r,x) for x in tL])
    return PL

print('\nThe following graph plots the growth of the principal sum over the given time horizon t = {} year(s)'.format(t))

PL = compound_interests_L(rL,P,tL)

#Plot the growth of the principal sum over the time horizon t at the given rates r in rL
import matplotlib.pyplot as plt
def compound_interest_plot(rL,P,t):
    data = compound_interests_L(rL,P,tL)
    for PL,r in zip(data,rL):
        label = "r = "+str(r)+"%"
        plt.plot(tL,PL,label=label)
    plt.xlabel("t [years]")
    plt.ylabel("Value [€]")
    plt.title("Compound Interest")
    plt.legend()
    plt.show()

compound_interest_plot(rL,P,t)
