filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filenames.replace('.', '-') + ".txt" for filenames in filenames]

print(filenames)