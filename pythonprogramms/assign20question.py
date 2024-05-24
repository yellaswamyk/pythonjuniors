#. Writ a script that prompts the user to enter hours and rate per hour. Calculate 
#pay of the person
def calculate_pay(hours, rate_per_hour):
    pay = hours * rate_per_hour
    return pay

try:
    hours_worked = float(input("Enter the number of hours worked: "))
    rate_per_hour = float(input("Enter the rate per hour: "))

    total_pay = calculate_pay(hours_worked, rate_per_hour)
    print("Total pay: $", total_pay)
except ValueError:
    print("Please enter valid numerical inputs for hours worked and rate per hour.")
