filenames = ["1. Raw Date.text", "2. Reports.txt", "3. Presentation.txt"]

for items in filenames:
    items = items.replace(".", "-", 1)
    print(items)


# Tuples: are immutable they can not be changed
