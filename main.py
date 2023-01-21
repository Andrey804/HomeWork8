from datetime import datetime, timedelta
from collections import defaultdict
import re

users = [
    {"name": "Bill",
     "birthday": datetime(year=1999, month=1, day=26)},
    {"name": "Jill",
     "birthday": datetime(year=2023, month=1, day=21)},
    {"name": "Kim",
     "birthday": datetime(year=2000, month=1, day=29)},
    {"name": "Jan",
     "birthday": datetime(year=1991, month=4, day=23)},
    {"name": "Mary",
     "birthday": datetime(year=2002, month=1, day=25)},
    {"name": "Anna",
     "birthday": datetime(year=1998, month=1, day=28)}
]


def get_birthdays_per_week(users_list):
    by_days = defaultdict(list)
    current_date = datetime.now()
    start_interval = current_date.date()
    end_interval = start_interval + timedelta(weeks=1)
    name_user = ""

    for user_dict in users_list:
        for k, v in user_dict.items():
            if k == "name":
                name_user = v
                continue

            user_with_current_year = v.replace(year=start_interval.year).date()

            if start_interval <= user_with_current_year <= end_interval:
                if start_interval.weekday() != 0:
                    if user_with_current_year.weekday() == 5 or user_with_current_year.weekday() == 6:
                        by_days["Monday"].append(name_user)
                    else:
                        by_days[user_with_current_year.strftime('%A')].append(name_user)
                else:
                    if user_with_current_year.weekday() != 5 and user_with_current_year.weekday() != 6:
                        by_days[user_with_current_year.strftime('%A')].append(name_user)

    for k, v in by_days.items():
        a = r'[\[\]\']'
        print(f"{k}: {re.sub(a, '', str(v))}")

get_birthdays_per_week(users)
