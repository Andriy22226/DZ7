from datetime import datetime, timedelta
from collections import defaultdict

friends = [
    {"name": "Emily","birthday": datetime(1999, 5, 29)
    },                                                                                                                        {"name": "Mary", "birthday": datetime(1997, 5, 29)
    },
    {"name": "William", "birthday": datetime(1995, 5, 30) 
    },
    {"name": "Justin", "birthday": datetime(1993, 5, 31) 
    },
    {"name": "Parker", "birthday": datetime(1985, 6, 2)
    },
    {"name": "Matt", "birthday": datetime(2003, 5, 27)
    },
]
def get_birthdays_per_week(friends):
    current_date = datetime.now() + timedelta(days=1)

    while current_date.weekday():
        current_date += timedelta(days=1)

    birthday_dict = defaultdict(list) 

    monday = current_date.date()

    previous_saturday = monday - timedelta(days=2)
    
    friday = (current_date + timedelta(days=4)).date()

    for friend in friends:
        friend_birthday = friend["birthday"].replace(year=current_date.year).date()
        if previous_saturday <= friend_birthday <= friday:
            if previous_saturday <= friend_birthday <= monday: 
                birthday_dict[monday].append(friend['name'])
            elif friend_birthday <= friday:
                birthday_dict[friend_birthday].append(friend["name"]) 
    for birthday in birthday_dict:
        print(f"{birthday.strftime('%A')}: {', '.join(birthday_dict[birthday])}")
    return friends
get_birthdays_per_week(friends)