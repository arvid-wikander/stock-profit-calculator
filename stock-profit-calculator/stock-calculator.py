import time
import os

print("Welcome to stock calculator xd")
time.sleep(0.5)

gav = ""
while gav < "0":
    gav = input("Enter Purchase Price (per share): ")
time.sleep(0.5)

shares = ""
while shares < "0":
    shares = input("Enter the amount of shares: ")

time.sleep(0.5)

total_gav = float(gav) * int(shares)

# print("Total purchase value:", (total_gav))

increase = ""
while increase < "0":
    increase = input("Current/Predicted future price of stock: ")

time.sleep(1)


profit_value = float(increase) * int(shares)

# print("Current/Predicted Total:", float(profit_value), "kr")

time.sleep(1)

profit = (float(profit_value - (float(total_gav))))


load = "Calculating Profit..."


for i in range(21):
    print(load[i], sep='', end= '', flush=True); time.sleep(0.1)
time.sleep(0.5)

print("\n\nTotal Profit:", (profit), "kr")

input('Press ENTER to exit')
