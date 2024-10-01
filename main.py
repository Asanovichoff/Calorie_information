from user import User
from training import TrainingSession

def main():
    user = User() 
    user.get_weight()

    session = TrainingSession(user.weight) 

    activity = session.get_activity()
    distance = session.get_distance(activity)
    calories_burned = session.calculate_calories(activity, distance)

    session.display_calories(activity, calories_burned)
    session.log_session_to_csv(activity, distance, calories_burned)

if __name__ == "__main__":
    main()
    
       
      
