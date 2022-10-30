from datetime import date

first_date = date(2022, 12, 10)
second_date = date(2022, 10, 1)

diference = second_date-first_date
# days = diference.days

# if days < 0:
#     days = days*(-1)

print(abs(diference.days))
