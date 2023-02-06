# A greedy algorithm to calculate change to give a customer.
def calculate_change(change_amount, denominations=None):
    if denominations is None:
        denominations = [25, 10, 5, 1]
        # denominations = [25, 10, 1]
    for denomination in denominations:
        while change_amount >= denomination:
            change_amount -= denomination
            print("Gave out", denomination, "cents. Remains", change_amount, "cents")

    print("You got your change, now bugger off.")


amount = int(input("Enter change amount: "))

use_default = input("Use default denominations [25, 10, 5, 1] (y/n): ")
if use_default == "y":
    calculate_change(amount)
elif use_default == "n":
    denoms = list(
        map(int, input("Enter the denominations, separated by spaces: ").split())
    )
    calculate_change(amount, denoms)
else:
    print("All you needed to do was enter a 'y' or 'n'. Now I'm angry, and I'm dead.")
