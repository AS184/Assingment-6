print("Enter number of concert tickets")
tickets = int(input())
ticket_price = 0
if tickets >= 25:
    ticket_price = 50
elif tickets >= 10 and tickets <= 24:
    ticket_price = 60
elif tickets >= 5 and tickets <= 9:
    ticket_price = 70
else:
    ticket_price = 75
total_price = tickets * ticket_price
print("Number of tickets: ", tickets)
print("Price per ticket: ", ticket_price)
print("Total cost: ", total_price)
