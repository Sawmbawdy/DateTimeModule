def cost_of_hotel(nights):
    return nights * 140
def destination(dest):
    DestCost = 0
    if dest == "Cairo":
        DestCost = 600
    elif dest == "Paris":
        DestCost = 750
    elif dest == "New York":
        DestCost = 800
    elif dest == "Tokyo":
        DestCost = 900
    return DestCost
def car_rental(days):
    cost_per_day = 40
    total_cost = days * cost_per_day
    if days >= 7:
        total_cost -= 50
    elif days >= 3:
        total_cost -= 20
    return total_cost
def trip_cost(city, days, spending_money):
    print("The hotel cost is:", cost_of_hotel(days))
    print("The cost of the flight is:", destination(city))
    print("The cost of car rental is:", car_rental(days))
    total = cost_of_hotel(days) + destination(city) + car_rental(days) + spending_money
    print("The total cost of the trip is:", total)

cost_of_hotel(3)
destination("Cairo")
car_rental(5)
trip_cost("Cairo", 5, 600)