print("Enter a part number")
part_number = int(input())
unit_price = 0
if part_number == 10 or part_number == 55: unit_price = 1.0
elif part_number == 99: unit_price = 2.0
elif part_number == 80 or part_number == 70: unit_price = 3.0
else: unit_price = 5.0
print("Enter a quantity ")
quantity = int(input())
total_price = quantity * unit_price
print("Part Number: ", part_number)
print("Unit Price: ", unit_price)
print("Total Price: ", total_price)