#quiz game

question = ("How many elements are there in a periodic table?",
            "Which animal lays the largest eggs?",
            "What is the most abudant gas in the earths atmosphere?",
            "Which planet in the solar system is the hotest?",
            "How many bones are in the human body?")

options = (("A.116","B.117","C.118","D.119"),
           ("A.whale","B.crocodile","C.ostrich","D.elephant"),
           ("A.Nitrogen", "B.oxygen", "C.CO2", "D.Hydrogen"),
           ("A.206", "B.207", "C.208", "D.209"),
           ("A.mercury", "B.venus", "C.earth", "D.mars"))


answers = ("C","D","A","A","D")
guesses = []
score = 0
Question_num = 0

for quiz in question:
    print("-------------------")
    print(quiz)
    for opt in options[Question_num]:
        print(opt)
    guess = input("Enter your answer(A, B, C , D)").upper()
    guesses.append(guess)
    if guess == answers[Question_num]:
        score += 1
        print("CORRECT!!!!!")
    else:
        print("INCORRECT!!!!!")
        print(f"{answers[Question_num]} is the correct answer.")

    Question_num += 1

print("--------------------")
print("           RESULTS           ")
print("--------------------")

print("answers:", end=" ")
for ans in answers:
    print(ans, end=" ")
print()

print("guesses:", end=" ")
for gues in guesses:
    print(gues, end=" ")
print()

