#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and 
#figure out at what x value y is going to be 0.
x_values = [-10, -5, 0, 5, 10]
for x in x_values:
    y = calculate_y(x)
    print(f"For x = {x}, y = {y}")
