from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
current_date = datetime.today()

if deadline_date < current_date:
    print("ear user! goal: {goal} is overdue")
else:
    left_time = deadline_date - current_date
    left_time_in_hours = int(left_time.total_seconds() / 60 / 60)
    print(f"Dear user! Time remaining for your goal: {goal} is {left_time_in_hours} hours")




