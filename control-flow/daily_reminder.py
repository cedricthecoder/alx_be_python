#declaring the variables
task_name = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

#case making
match task_priority:
    
    case "high": 
        if time_bound == "yes":
            print(f"{task_name} is a {task_priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"{task_name} is a {task_priority} priority task that requires you to delegate!")
        else:
            print("Something went wrong. Please try again.")
    
    case "medium": 
        if time_bound == "yes":
            print(f"{task_name} is a {task_priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"{task_name} is a {task_priority} priority task that you can complete in your free time!")
        else:
            print("Something went wrong. Please try again.")
    
    case "low": 
        if time_bound == "yes":
            print(f"{task_name} is a {task_priority} priority task that requires you to ignore or delegate it today!")
        elif time_bound == "no":
            print(f"{task_name} is a {task_priority} priority task. Consider completing it when you have free time.")
        else:
            print("Something went wrong. Please try again.")
    case _:
        print("Something went wrong. Please try again.")
