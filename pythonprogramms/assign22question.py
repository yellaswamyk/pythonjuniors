#2. Write a script that prompts the user to enter number of years. Calculate the 
#number of seconds a person can live. Assume a person can live hundred years
def main():
    years = int(input("Enter the number of years: "))
    seconds_in_minute = 60
    minutes_in_hour = 60
    hours_in_day = 24
    days_in_year = 365
    years_in_century = 100

    seconds_in_century = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year * years_in_century

    seconds_lived = years * seconds_in_century / years_in_century

    print("A person can live approximately", seconds_lived, "seconds.")

if __name__ == "__main__":
    main()
