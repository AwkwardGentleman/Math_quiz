import random


def give_questions():
    first_num = random.randint(1, 50)
    second_num = random.randint(1, 50)
    equations = [f"{first_num} + {second_num}",
                 f"{first_num} - {second_num}"]

    equation_shown = random.choice(equations)
    answer = eval(equation_shown)
    user_answer = input(f"{equation_shown} = ")
    while user_answer != float:
        try:
            user_answer = float(user_answer)
            break
        except ValueError:
            print(f"{user_answer} is not a number")
            user_answer = input(f"{equation_shown} = ")
    if user_answer == answer:
        print("correct")
    else:
        print(f"incorrect, answer = {answer}")


while True:
    give_questions()
