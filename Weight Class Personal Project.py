
user_weight = float(input("Enter your weight: "))



if user_weight <= 115:
    print("You are strawweight.")
elif user_weight <= 125:
    print("You are flyweight.")
elif user_weight <= 135:
    print("You are bantamweight.")
elif user_weight <= 145:
    print("You are featherweight.")
elif user_weight <= 155:
    print("You are lightweight.")
elif user_weight <= 165:
    print("You are super lightweight.")
elif user_weight <= 170:
    print("You are welterweight.")
elif user_weight <= 175:
    print("You are super welterweight.")
elif user_weight <= 185:
    print("You are middleweight.")
elif user_weight <= 195:
    print("You are super middleweight.")
elif user_weight <= 205:
    print("You are light heavyweight.")
elif user_weight <= 225:
    print("You are cruiserweight.")
elif user_weight <= 265:
    print("You are heavyweight.")
elif user_weight > 265:
    print("You are super heavyweight.")
else:
    print("Please enter a valid weight.")



