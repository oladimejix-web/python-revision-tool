questions = {
    "What is the powerhouse of the cell?": "mitochondria",
    "What is the equation for density?": "mass / volume",
    "What is the charge of an electron?": "-1"
}

score = 0

print("A-Level Revision Tool")
print("---------------------")

for question, answer in questions.items():
    user_answer = input(question + "\n> ")

    if user_answer.lower().strip() == answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The answer was: {answer}\n")

print(f"You scored {score}/{len(questions)}.")
