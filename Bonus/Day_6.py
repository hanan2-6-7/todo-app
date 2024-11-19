contents = ["All carrots are to be sliced logitudinaly.",
            "The carrot were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "prentation.txt"]

for contents, filenames in zip(contents, filenames):
    file = open(f"../files/{filenames}", "w")
    file.write(contents)


a = ("helowor"
     "lditsme")