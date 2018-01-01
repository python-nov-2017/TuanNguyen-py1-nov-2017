def change(cents):
    coins = {}
    (coins["dollars"], cents) = divmod(cents, 100)
    (coins["quarters"], cents) = divmod(cents, 25)
    (coins["dimes"], cents) = divmod(cents, 10)
    (coins["nickles"], cents) = divmod(cents, 5)
    coins["pennies"] = cents
    return coins


coins = change(387)

print coins