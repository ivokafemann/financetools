"""
A small tool to calculate the value of an investment in the future.

Asks the user how much money and at what interest rate he wants to invest.

Args:
    (int) P - value of initial investment
    (int) r - interest rate
    (int) t - time in years
Returns:
    (int) P1 - Value of investment in the future
"""

P = int(input('\nHow much money would you like to invest?\n'))
r = int(input('\nWhat is the interest rate (write only 5 for an interest rate 5 %) for the investment?\n'))
t = int(input('\nWhat is the time horizon in years for the investment?\n'))

#Annuity Function
def compound_interest(P,r,t):
    P1 = P * (1 + r/100)**t
    return P1

print('\nThe value of your investment after {} year(s) at an interest rate of {}% is: {}'.format(t,r,compound_interest(P,r,t)))

#Create a list of annuities with the Annuities Function
def compound_interests(P,r,t):
    P1 = [compound_interest(P,r,x) for x in range(t)]
    return P1

print('\nThe annuity for each year is shown in the following list:\n',compound_interests(P,r,t))
print('\nThe following graph plots the annuities over the given time horizon T\n')

tL = list(range(t))

#Plot the annuities over the time horizon T
import matplotlib.pyplot as plt
plt.plot(tL,compound_interests(P,r,t))
plt.xlabel("t [y]")
plt.ylabel("Value [€]")
plt.title("Compound Interest")
plt.show()
