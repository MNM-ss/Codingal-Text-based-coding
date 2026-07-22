print("====================================")
print("     Welcome to Holiday Planner!    ")
print(" Build a perfect holiday plan for u   ")
print("====================================")
print()

print("Step 1: Pick your Holiday")
print("  1 - Summer vacation")
print("  2 - Winter Break")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    # Nested if-else — runs only when choice is 1
    print("Step 2: Pick your summer dream")
    print("  1 - Relaxation from heat")
    print("  2 - Fun water time and ativities")
    print()

    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("You picked  : Relaxation from heat")
        print("Top tips   : Drink plenty of water, wear loose cloths and stay in shade for maximum relaxation!")
        print("Best for    : Old people, heat affected people, Pregenant women or injured people")
    else:
        print("You picked  : Fun water time and ativities")
        print("Top tips   : Play games like summer tag, go to the beach or local pool, eat plenty of ice cream but be careful to not get sick!")
        print("Best for    : Children, Busy Students, Teens.")

elif choice == 2:
    # Nested if-else, runs only when choice is 2
    print("Step 2: Pick your Winter Checklist")
    print("  1 - Cozy winter")
    print("  2 - Winter adventures")
    print()

    car_type = int(input("Enter 1 or 2: "))
    print()
    
    
    if car_type == 1:
        print("You picked  : Sedan")
        print("Passenger Count   : 5 passengers")
        print("Best for    : City roads")
    else:
        print("You picked  : SUV")
        print("Passenger Count   : 7 passengers")
        print("Best for    : Off-road adventures")

else: 
    print("That was not a valid option!")
    print("choose 1 or 2")
    print()


print("====================================")
print("   Hope you enjoyed Ride Builder!   ")
print("====================================")
