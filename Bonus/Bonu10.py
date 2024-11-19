try:
    width = int(input("Enter rectangle width: "))
    height = int(input("Enter rectangle height: "))

    if width == height:
        exit("That looks a square!")
    area = width * height
    print(area)
except ValueError:
    print("Please Enter a number.")