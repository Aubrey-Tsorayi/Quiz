from Question import Question

questions_prompts = [
    "What is Newton's second law of motion?\n(a) F = ma\n(b) P = VI\n(c) W = mg\n\n",
    "When was the first computer created?\n(a) 1954\n(b) 1943\n(c) 1940\n\n",
    "Who invented the light buld?\n(a) Nikola Tesla\n(b) Rudolf Diesel\n(c) Thomas Edison\n\n",
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        answer = input(">>")
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)