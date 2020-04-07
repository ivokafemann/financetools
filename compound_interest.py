"""
A small tool to calculate the value of an investment in the future.

Asks the user how much money, at which interest rate he wants to invest.

Args:
    (int) I - value of initial investment
    (int) r - interest rate
    (int) t - time in years
Returns:
    (int) A - Value of investment in the future
"""

I = int(input('\nHow much money would you like to invest?\n'))
r = int(input('\nWhat is the interest rate (write only 5 for an interest rate 5 %) for the investment?\n'))
t = int(input('\nWhat is the time horizon in years for the investment?\n'))

def terminal_value(I,r,t):
    T = I * (1 + r/100)**t

    return T

print('\nThe value of your investment after {} year(s) at an interest rate of {}% is: {}'.format(t,r,terminal_value(I,r,t)))
