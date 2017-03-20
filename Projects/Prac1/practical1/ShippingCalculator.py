number_of_items = int(input("Enter number of items: "))
total_cost = 0  # Init
for i in range(number_of_items, 0, -1):
    total_cost += float(input("Enter Cost of item: "))
if total_cost >= 100:
    total_cost *= 0.9


print("The total cost for your {:.2f} item(s)".format(number_of_items), " is ${:.2f}".format(total_cost))
