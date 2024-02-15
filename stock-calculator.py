import time
import os
import click

def main():
    os.system('cls')

    currency=input("In what currency do you want to calculate?: ")
    
    gav = ""
    while gav < "0":
        gav = input("Enter Purchase Price (per share): ")
    time.sleep(0.5)

    shares = ""
    while shares < "0":
        shares = input("Enter the amount of shares: ")

    time.sleep(0.5)

    total_gav = float(gav) * int(shares)

    increase = ""
    while increase < "0":
        increase = input("Current/Predicted future price of stock: ")

    profit_value = float(increase) * int(shares)
    time.sleep(0.1)
    profit = (float(profit_value - (float(total_gav))))

    load = "Calculating Profit..."

    for i in range(21):
        print(load[i], sep='', end= '', flush=True); time.sleep(0.05)
    time.sleep(0.1)

    print("\n\nTotal Profit:", (profit), (currency))
    confirm=click.confirm("\nRestart?", default=False)
    if confirm==True:
        return
    else:
        quit()

while True:
    main()

exit()
