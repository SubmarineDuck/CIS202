muffins = 10  # starting stock
cupcakes = 10

while True:
    customer_order = input().lower()  # in case they enter capital first letter

    if customer_order == "muffin":  # ordering a muffin
        if muffins > 0:
            muffins -= 1
        else:
            print("Out of stock")
    elif customer_order == "cupcake":  # ordering a cupcake
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Out of stock")
    elif customer_order == "0":  # customer is done ordering
        break

print("muffins:", muffins,"cupcakes:", cupcakes)  # output of order
