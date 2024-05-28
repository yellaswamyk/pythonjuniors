#Write a Python script that displays the following table
def main():
    print("Number\tSquare\tCube")
    print("------\t------\t------")
    for i in range(1, 11):
        square = i ** 2
        cube = i ** 3
        print(f"{i}\t{square}\t{cube}")
if __name__ == "__main__":
    main()
