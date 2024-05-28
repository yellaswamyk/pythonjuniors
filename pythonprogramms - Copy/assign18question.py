#Check if type of '10' is equal to type of 10
type_of_str = type('10')
type_of_int = type(10)

if type_of_str == type_of_int:
    print("The type of '10' is equal to the type of 10.")
else:
    print("The type of '10' is not equal to the type of 10.")
