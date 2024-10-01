class User:
    def __init__(self):
        self.weight = None

    def get_weight(self):
        while True:
            try:
                self.weight = float(input("What was your weight in kg before training?: "))
                break
            except ValueError:
                print("Please enter a valid number for weight.")