#All converting methots was obtained from PhD-level empirical data points
try:
    weight = float(input("What was your weight in kg before training?: "))
except ValueError:
    print("Please enter a valid number for weight.")
    exit()
todays_training = input("What did you do today?: Swim, Bike or Run: ").strip().lower()
if todays_training == "swim":
    try:
        swim_distance = int(input("How many metrs did you swim?: "))   
        burned_swim_calories = ((3.83 * weight)/1000)*swim_distance
        print(f"You burned : {burned_swim_calories}calories")
    except ValueError:
        print("Please enter a valid number for distance.")
elif todays_training == "bike":
    try:
        bike_distance = int(input("How many km did you bike?: "))
        burned_bike_calories = (0.29 * weight)*bike_distance
        print(f"You burned : {burned_bike_calories}calories")
    except ValueError:
        print("Please enter a valid number for distance.")
elif todays_training == "run":
    try:
        run_distance = int(input("How many km did you run?: "))
        burned_run_calories = (1.036 * weight)* run_distance
        print(f"You burned : {burned_run_calories}calories")
    except ValueError:
        print("Please enter a valid number for distance.")    
else:
    print("Didn't understand your input. Please type 'Swim', 'Bike', or 'Run'.")
    
       
       
      
