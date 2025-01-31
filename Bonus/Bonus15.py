import json

with open("question.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternatives in enumerate(question["alternatives"]):
        print(index + 1, "-", alternatives)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = (f"{index + 1} {result}  - Your answer: {question['user_choice']}, "
               f"correct answer: {question['correct_answer']}")
    print(message)

print(data)
print(score, "/", len(data))

