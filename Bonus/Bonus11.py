def get_average():
    with open("data.txt", "r") as file:
        data = file.readlines()

    value = data[1:]
    value = [float(i) for i in value]

    locale_average = sum(value) / len(value)
    return locale_average


average = get_average()
print(average)

print(get_average())


