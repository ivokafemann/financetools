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

def terminal_value(I,r,T):
    T0 = I * (1 + r/100)**T
    return T0

print('\nThe value of your investment after {} year(s) at an interest rate of {}% is: {}'.format(T,r,terminal_value(I,r,T)))

def annuity(I,r,T):
    A = [terminal_value(I,r,x) for x in range(T)]
    return A

print('\nThe annuity for each year is shown in the following list:\n',annuity(I,r,T))
