"""
A small tool to calculate the value of an investment in the future.

Asks the user how much money and at what interest rate he wants to invest.

Args:
    (int) I - value of initial investment
    (int) r - interest rate
    (int) T - time in years
Returns:
    (int) A - Value of investment in the future
"""

I = int(input('\nHow much money would you like to invest?\n'))
r = int(input('\nWhat is the interest rate (write only 5 for an interest rate 5 %) for the investment?\n'))
T = int(input('\nWhat is the time horizon in years for the investment?\n'))

#Annuity Function
def annuity(I,r,t):
    A = I * (1 + r/100)**t
    return A

print('\nThe value of your investment after {} year(s) at an interest rate of {}% is: {}'.format(T,r,annuity(I,r,T)))

#Create a list of annuities with the Annuities Function
def annuities(I,r,T):
    A = [annuity(I,r,x) for x in range(T)]
    return A

print('\nThe annuity for each year is shown in the following list:\n',annuities(I,r,T))
print('\nThe following graph plots the annuities over the given time horizon T\n')

t = list(range(T))

#Plot the annuities over the time horizon T
import matplotlib.pyplot as plt
plt.plot(t,annuities(I,r,T))
plt.xlabel("t")
plt.ylabel("Value")
plt.title("Annuities")
plt.show()
