# Input for function parameters
purchasePrice = float(input("Please indicate purchase value : "))
customerPay = int(input("Please indicate amount given by customer : "))

def fx_give_change(purchase_amount: float, customer_amount: int):
    """
    Return the detail of the change to be given to a customer
    based on purchasing price and amount provided by customer
    """
    # List of possible notes and coins
    bill_coin = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    # Empty list to collect change values
    give_change = []

    # Round change to 2 digits
    change_amount = round(customer_amount - purchase_amount, 2)
    test_change_amount = round(customer_amount - purchase_amount, 2)

    # Loop on every element of possible notes and coins list
    for elem in bill_coin:
        # If change amount equal or below zero, break the loop
        if change_amount <= 0:
            break
        # While remaining change is higher to selected note or coin
        # Add it to give_change list and decrease change_amount by the same value
        while round(change_amount, 2) >= elem:
            give_change.append(elem)
            change_amount -= elem

    # Build a list of unique values from give_change list
    # We convert to a set and then back to a list to sort it
    change_unique_set = set(give_change)
    change_unique_list = list(change_unique_set)
    change_unique_list.sort(reverse=True)

    # Build an empty list to collect the results
    final_change = []
    # Loop on every element of unique change list
    # Append result list with the result according to the note or coin value
    for elem in change_unique_list:
        if elem >= 5:
            final_change.append(
                f"Nb {elem} euros notes: {give_change.count(elem)}")
        elif elem >= 1:
            final_change.append(
                f"Nb {elem} euros coins: {give_change.count(elem)}")
        else:
            final_change.append(
                f"Nb {int(elem * 100)} cents coins: {give_change.count(elem)}")

    # Declare result variable to collect results as a string
    result = ""
    # Final according to change amount to select what to display
    if test_change_amount < 0:
        result = print("Customer didn't give enough money")
    elif test_change_amount == 0:
        result = print("No change to provide")
    elif test_change_amount > 0:
        result = print("\n".join(final_change))

    # Join result from the list and display each element on a distinct line
    return result


fx_give_change(purchasePrice, customerPay)