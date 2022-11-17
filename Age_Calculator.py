import datetime
from pywebio.input import *
from pywebio.output import *

def Age_Calculator():
    '''create a python function that takes user birth year & month & day and prints
how old is he and next birth date      ___must enter(11/11/1111)
'''
    while True:
        # print("x"*50)  # WELCOME program
        name = input("please enter your name :".title())  # enter user name
        today = datetime.date.today()  # get current date
        # input birthdate must be (11/11/1111)
        birth = (input("enter your birth date please :".title()))
        birth_day, birth_month, birth_year = int(birth.split("/")[0],), int(birth.split(
            "/")[1]), int(birth.split("/")[2])  # convert input string to list to handle it
        age_days, age_month, age_year = abs(today.day-birth_day), abs(
            today.month-birth_month), abs(today.year-birth_year)  # get user age (days&months&years)
        if today.month < birth_month and birth_month > 12:
            next_birthdate = datetime.date(today.year, birth_month, birth_day)
            num_days = next_birthdate-today
            month_left = int(num_days.days)//30
            days_left = int(num_days.days) % 30
        else:
            next_birthdate = datetime.date(
                today.year+1, birth_month, birth_day)
            num_days = next_birthdate-today
            month_left = int(num_days.days)//30
            days_left = int(num_days.days) % 30
        put_table([[f"welcome {name} \nyour age is".title(), f"{age_year}\nyears", f"{age_month}\nmonths", f"{age_days}\ndays", f"birthday after\n{month_left}-months & {days_left}-days ".title()], ], header=[
            'Name', "Year", 'Month', "Days", "Next_birthday"]).style('color: yellow; font-size: 25px')

if __name__ == "__main__":
    Age_Calculator()  # run program
