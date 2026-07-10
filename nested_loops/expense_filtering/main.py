# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],[200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70], [400, 320, 110, 100],
                [550, 270, 180, 60], [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85], [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []

for travel_cost in travel_costs:
    item_index = 0
    travel_cost_new = []
    for item_index in range(0,len(travel_cost)):
        if travel_cost[item_index] <= 100:
            travel_cost_new.append("Cheap")
        else:
            travel_cost_new.append(travel_cost[item_index])
        item_index += 1
    processed_expenses.append(travel_cost_new)

# Testing
print('Processed Travel Expenses:', processed_expenses)