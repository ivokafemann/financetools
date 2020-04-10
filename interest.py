"""
A small tool to calculate the value of an investment in the future.

Asks the user how much money and at what interest rate he wants to invest.

Args:
    (int) P - value of initial investment
    (int) r - interest rate
    (int) t - time in years
Returns:
    (int) Pt - Value of investment in the future after t years
"""

P = int(input('\nHow much money would you like to invest?\n'))
r = int(input('\nWhat is the interest rate (write only 5 for an interest rate 5 %) for the investment?\n'))
t = int(input('\nWhat is the time horizon in years for the investment?\n'))

#Compound Interest Function
def compound_interest(P,r,t):
    Pt = P * (1 + r/100)**t
    return Pt

print('\nThe value of your investment after {} year(s) at an interest rate of {}% is: {}'.format(t,r,compound_interest(P,r,t)))

#Create a list of compound interests for all moments of the time horizon with the compound_interest function
def compound_interests(P,r,t):
    PL = [compound_interest(P,r,x) for x in range(t)]
    return PL

print('\nThe new principal sum at each year is shown in the following list:\n',compound_interests(P,r,t))
print('\nThe following graph plots the growth of the principal sum over the given time horizon t = {} year(s)'.format(t))

tL = list(range(t+1))

##Plot the growth of the principal sum over the time horizon t at the given rate r
import matplotlib.pyplot as plt
plt.plot(tL,compound_interests(P,r,t))
plt.xlabel("t [y]")
plt.ylabel("Value [€]")
plt.title("Compound Interest")
plt.show()
