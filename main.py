class HealthFitnessManagementSystem:
    
    def __init__(self):
        self.daily_logs = []
        self.goals = {
            'calories': None,
            'exercise_minutes': None,
            'water_liters': None  
        }
        
    def set_goals(self):
        print("\nSet your fitness goals:")
        self.goals['calories'] = int(input("Enter daily calorie goal: "))
        self.goals['exercise_minutes'] = int(input("Enter daily exercise minutes goal: "))
        self.goals['water_liters'] = float(input("Enter daily water intake goal (liters): "))
        print("Goals set successfully!\n")
        
    def log_entry(self):
        date = input("Enter the date (YYYY-MM-DD): ")
        calories = int(input("Enter calories consumed: "))
        exercise_minutes = int(input("Enter exercise minutes: "))
        water_liters = float(input("Enter water intake (liters): "))
        
        entry = {
            'date': date,
            'calories': calories,
            'exercise_minutes': exercise_minutes,
            'water_liters': water_liters
        }
        
        self.daily_logs.append(entry)
        print("Entry added successfully!\n")
        
    def display_summary(self):
        if not self.daily_logs:
            print("No logs available.")
            return
    
        print("\nHealth and Fitness Summary:")
                
        for log in self.daily_logs:
            print(f"Date: {log['date']}")
            print(f"Calories Consumed: {log['calories']} / {self.goals['calories']} (Goal)")
            print(f"Exercise minutes: {log['exercise_minutes']} / {self.goals['exercise_minutes']} (Goal)")
            print(f"Water intake: {log['water_liters']} liters / {self.goals['water_liters']} liters (Goal)")
            print("_" * 30)
            
    def start(self):
        while True:
            print("\nHealth and Fitness Management System")
            print("1. Set Goals")
            print("2. Log Today's Entry")
            print("3. Display Summary")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                self.set_goals()
            elif choice == "2":
                self.log_entry()
            elif choice == "3":
                self.display_summary()
            elif choice == "4":
                print("Exiting the System. Stay Healthy!")
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    system = HealthFitnessManagementSystem()
    system.start()
