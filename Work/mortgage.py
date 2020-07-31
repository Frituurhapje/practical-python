# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0
interest_paid = 0
total_redemption = 0

while principal > 0:
    interest_payment = principal * rate
    redemption = payment - interest_payment
    principal -= redemption
    total_paid += payment
    interest_paid += interest_payment
    total_redemption += redemption
    print()


