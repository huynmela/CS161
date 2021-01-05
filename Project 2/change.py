# Author: Melanie Huynh
# Date: 4/8/2020
# Description: This asks for an amount in cents less than a dollar and outputs how many of each type of coin would represent that amount with the fewest total number of coins.

print("Please enter an amount in cents less than a dollar.") 
cents = int(input())

Q_amount = cents // 25
Q_mod = cents % 25

D_amount = Q_mod // 10
D_mod = Q_mod % 10

N_amount = D_mod // 5
N_mod = D_mod % 5

P_amount = N_mod // 1
P_mod = N_mod % 1

print("Your change will be:")

print("Q:", Q_amount)
print("D:", D_amount) 
print("N:", N_amount)
print("P:", P_amount)
