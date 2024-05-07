import datetime

def get_namazi_name():
    group_members = ["Atta & Talha", "Atta & Zaf", "Fizan & Adeel"]
    current_date = datetime.datetime.now()
    week_number = current_date.isocalendar()[1]  # Get the week number of the year
    Friday_index = week_number % len(group_members)  # Calculate the index for this week
    return group_members[Friday_index]

namazi_name = get_namazi_name()
print(f"It is {namazi_name}'s turn to go Jumah this week.")
