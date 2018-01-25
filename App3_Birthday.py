import datetime


def print_header():
    print('--------------------------------')
    print('        BIRTHDAY APP :)')


def get_birthday_from_user():
    print('--------------------------------')
    print('      When were you born:')
    month = int(input('      Month [MM]:  '))
    day = int(input('      Day   [DD]:  '))
    year = int(input('      Year[YYYY]:  '))
    print('--------------------------------')


    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_bday_info(days):
    if days < 0:
        print()
        print('Your birthday is in {} days!'.format(-days))
    elif days > 0:
        print()
        print('You had your birthday already this years! {} days ago'.format(days))
    else:
        print()
        print('Happy Birthday!!!')
    print()
    print('--------------------------------')
    print()


def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between(bday, now)
    print_bday_info(number_of_days)


main()