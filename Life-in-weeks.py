age = input("What is your current age?\n")

age = int(age)

days_till_90 = 90 * 365
weeks_till_90 = 90 * 52
months_till_90 = 90 * 12

days_lived = age * 365
weeks_lived = age * 52
months_lived = age * 12

days_left = days_till_90 - days_lived
weeks_left = weeks_till_90 - weeks_lived
months_left = months_till_90 - months_lived

day = "days"
week = "weeks"
month = "months"

print(
    f"You have {days_left} {day}, {weeks_left} {week}, and {months_left} {month} left if you live till 90."
)
