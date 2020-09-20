# for sauna users, it’s 1500 HUF altogether
# for the ones who don’t intend to use the sauna, the following applies: (unless they are students):
# women: 500 HUF
# men: 750 HUF
# for students it’s 300 HUF (unless they use the sauna)
# below the age of 14, usage of the gym is forbidden

questions = ["Are you older than 14 years old? (y/n)", "Do you want to use the sauna? (y/n)",
             "Are you a student? (y/n)", "What is your gender? (m/f)"]


def reception_simple():
    global questions
    answer = input(questions[0])
    if answer.lower() == "y":
        answer = input(questions[1])
        if answer.lower() == "y":
            print("Your ticket will be 1500 HUF")
        elif answer.lower() == "n":
            answer = input(questions[2])
            if answer.lower() == "y":
                print("Your ticket will be 300 HUF")
            elif answer.lower() == "n":
                answer = input(questions[3])
                if answer.lower() == "m":
                    print("Your ticket will be 750 HUF")
                elif answer.lower() == "f":
                    print("Your ticket will be 500 HUF")
                else:
                    print("Sorry I don't understand you.")
            else:
                print("Sorry I don't understand you.")
        else:
            print("Sorry I don't understand you.")
    elif answer.lower() == "n":
        print("Sorry you can't enter.")
    else:
        print("Sorry I don't understand you.")


def reception_complex():
    global questions

    answers = [{"y": 1, "n": -1}, {"y": -1, "n": 2},
               {"y": -1, "n": 3}, {"m": -1, "f": -1}]

    prices = {
        (0, "n"): "Sorry you can't enter.",
        (1, "y"): "Your ticket will be 1500 HUF",
        (2, "y"): "Your ticket will be 300 HUF",
        (3, "m"): "Your ticket will be 750 HUF",
        (3, "f"): "Your ticket will be 500 HUF"
    }

    question = 0

    while True:
        answer = input(questions[question])
        if answer.lower() in answers[question]:
            next_question = answers[question][answer.lower()]
            if next_question != -1:
                question = next_question
            else:
                print(prices[(question, answer.lower())])
                break
        else:
            print("Sorry I don't understand you.")


reception_simple()
reception_complex()
