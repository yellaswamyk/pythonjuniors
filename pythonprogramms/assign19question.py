#Check if int('9.8') is equal to 10
try:
    converted_int = int(float('9.8'))
    if converted_int == 10:
        print("int('9.8') is equal to 10.")
    else:
        print("int('9.8') is not equal to 10.")
except ValueError:
    print("Conversion failed: '9.8' is not a valid integer string.")
