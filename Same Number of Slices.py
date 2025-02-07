slices_per_person = int(input("How many slices will everyone have? "))
if slices_per_person < 0:  # checking for negative
    exit("Invalid input. Slices cannot be negative.")
else:
    total_slices = slices_per_person * 4
    pizzas_required = (total_slices + 7) // 8  # rounding up
    leftover_slices = (pizzas_required * 8) - total_slices
    print("You Need", pizzas_required, "pizzas", end=" ")
    print("and will have", leftover_slices, "slices left")
