class TrainingSession:
    def __init__(self, weight):
        self.weight = weight

    def get_activity(self):
        while True:
            activity = input("What did you do today? (Swim, Bike, Run): ").strip().lower()
            if activity in ['swim', 'bike', 'run']:
                return activity
            else:
                print("Invalid input. Please type 'Swim', 'Bike', or 'Run'.")

    def get_distance(self, activity):
        while True:
            try:
                if activity == 'swim':
                    distance = float(input(f"How many meters did you swim?: "))
                else:
                    distance = float(input(f"How many kilometers did you {activity}?: "))
                return distance
            except ValueError:
                print("Please enter a valid number for distance.")

    def calculate_calories(self, activity, distance):
        if activity == "swim":
            return ((3.83 * self.weight) / 1000) * distance
        elif activity == "bike":
            return 0.29 * self.weight * distance
        elif activity == "run":
            return 1.036 * self.weight * distance

    def display_calories(self, activity, calories_burned):
        print(f"You burned: {calories_burned:.2f} calories doing {activity.capitalize()}")