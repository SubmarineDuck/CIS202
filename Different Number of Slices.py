person_1 = int(input("How many slices for person 1? "))
if person_1 < 0: exit("Invalid input. Slices cannot be negative.")  # checking for negative
person_2 = int(input("How many slices for person 2? "))
if person_2 < 0: exit("Invalid input. Slices cannot be negative.")
person_3 = int(input("How many slices for person 3? "))
if person_3 < 0: exit("Invalid input. Slices cannot be negative.")
person_4 = int(input("How many slices for person 4? "))
if person_4 < 0: exit("Invalid input. Slices cannot be negative.")
total_slices = person_1 + person_2 + person_3 + person_4

pizzas_required = (total_slices + 7) // 8  # rounding up
leftover_slices = (pizzas_required * 8) - total_slices
print("You Need", pizzas_required, "pizzas", end=" ")
print("and will have", leftover_slices, "slices left")
