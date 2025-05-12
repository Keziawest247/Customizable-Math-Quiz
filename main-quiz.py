"Customizable Math Quiz"
import random as ra

def choose_question_type() -> str:
    """Ask user for preferred type of maths question.

    The user is prompted to make a choice from the options available.
    The loop will continue to ask whilst their choice is not one of the
    available options from the list.

    Returns:
        The type of question to be used in the quiz.
    """
    # Define a list of choices
    question_type = ["Addition", "Multiplication", "Subtraction", "Division", "Modulus", "Exponentiation" ,"Mix"] # Extend: Division, Modulus, Exponentiation
    print(f"Choose a question type: {", ".join(question_type)}\n") #join comma and
    choice = input("Enter Choice: ").title()

    while choice not in question_type:
        choice = input("Try again: ").title()
    else:
        return choice


def generate_numbers_for_questions(difficulty_level: int) -> tuple:
    """Generate the numbers needed for the questions.

    Difficulty level 1: numbers 2 - 20
    Difficulty level 2: numbers 4 - 40
    Difficulty level 3: numbers 6 - 60
    Difficulty level 4: numbers 8 - 80
    Difficulty level 5: numbers 10 - 100

    Args:
        difficulty_level: A number from 1-5 relating to the difficulty of the question.

    Returns:
        A tuple of 2 numbers to be used in the question.
    """
    operand_a = ra.randint(difficulty_level *2, difficulty_level*20)
    operand_b = ra.randint(difficulty_level *2, difficulty_level *20)
    return operand_a, operand_b


def choose_number_of_questions() -> int:
    """Ask user for number of questions they'd like to answer.

    Returns:
        the number of questions, which will determine loop size.
    """
# Fetch user input to determine types of questions to be asked.
    try:
        num_of_questions = int(input("how many questions?"))
    except ValueError:
        print("Incorrect, defaulting to 10.")
        return 10
    else: # if no ValueError is raise
        if num_of_questions <= 0:
            print("Invalid Number, defaulting to 10.")
            return 10
        return num_of_questions


def choose_difficulty_level() -> int:
    """Ask user to chosen a difficulty level.

    In the quiz we have 5 difficulty levels (1-5), where 1 is
    the easiest and 5 is the hardest. The difficulty level will
    be used later when generating questions. The higher the
    difficulty, the larger the numbers that are used.

    Returns:
        and integer from 1-5 representing difficulty level.
    """
    while True: #infinite While Loop; happen forever, stop by having a range.
        try:
            difficulty_level = int(input("Choose a level from 1-5: ")) # ask user
        except ValueError:
            print("Invalid format, try again.")
            continue ### stop here and jump back to try, keep cycle
        else:
            if difficulty_level in range(1, 6): # put difficulty level range in place
                return difficulty_level
            print("Number must be between 1-5")
            continue


def addition_question(operand_a: int, operand_b: int) -> bool:
    """Ask addition question, returning True if correct and False otherwise.

    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """
    try:
        question = int(input(f"What is {operand_a} plus {operand_b}? ")) # 12
    except ValueError:
        print("Invalid format, moving on to next question.")
        return False
    else:
        return True if (question == operand_a + operand_b) else False# if 12 = 12 return True


def subtraction_question(operand_a: int, operand_b: int) -> bool:
    """Ask subtraction question, returning True if correct and False otherwise.

    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """
    try:
        question = int(input(f"What is {operand_a} minus {operand_b}? ")) # 12
    except ValueError:
        print("Invalid format, moving on to next question.")
        return False
    else:
        return True if (question == operand_a - operand_b) else False


def multiplication_question(operand_a: int, operand_b: int) -> bool:
    """Ask multiplication question, returning True if correct and False otherwise.

    Args:
        operand_a: The first operand used to construct the question.
        operand_b: The first operand used to construct the question.

    Returns:
        True or False depending on if answer is correct.
    """
    try:
        question = int(input(f"What is {operand_a} multiplied by {operand_b}? ")) # 12
    except ValueError:
        print("Invalid format, moving on to next question.")
        return False
    else:
        return True if (question == operand_a * operand_b) else False


def division_question(operand_a: int, operand_b: int) -> bool:
    """Ask a division question and return True If correct."""
    try:
        question = int(input(f"What is {operand_a} divided by {operand_b}? ")) # 12
    except ValueError:
        print("Invalid format, moving on to next question.")
        return False
    else:
        return True if (question == operand_a / operand_b) else False


def modulus_question(operand_a: int, operand_b: int) -> bool:
    """Ask an modulus question and return True if correct."""
    try:
        question = int(input(f"What is {operand_a} divisble by {operand_b}? ")) # 12
    except ValueError:
        print("Invalid format, moving on to next question.")
        return False
    else:
        return True if (question == operand_a % operand_b) else False


def exponentiation_question(operand_a: int, operand_b: int) -> bool:
    """Ask an exponentiation question and return True if correct."""
    try:
        question = int(input(f"What is {operand_a} to the power of {operand_b}? "))
    except ValueError:
          print("Invalid format, moving on to next question.")
          return False
    else:
          return True if (question == operand_a ** operand_b) else False


def main_game_loop(question_type: str, num_of_questions: int, difficulty_level: int) -> int:
    """Orchestrate the question loop and score keeping.

    This function consists of a for loop which loops for as many times as 'difficulty_level'
    For each cycle of the loop, the question type is examined which either picks a 'fixed' question
    or in the case when 'Mix' is selected a random question is chosen from the list. The score is kept
    during the quiz and incremented for each correct answer.

    Args:
        question_type: The type of questions to select (which function to call).
        num_of_question: Number of questions to answer (How long the loop runs for).
        difficulty_level: Determines the numbers to come from 'generate_numbers_for_question'.

    Returns:
        The number of correctly answered questions.
    """
    num_of_correct_answers = 0
    for i in range(1, num_of_questions+1):
        operand_a, operand_b = generate_numbers_for_questions(difficulty_level)
        ### Generate random numbers.
        print(operand_a, operand_b)
        print(f"Questions: {i}")
        if question_type == "Addition":
            response = addition_question(operand_a, operand_b)
        elif question_type == "Subtraction":
            response = subtraction_question(operand_a, operand_b)
        elif question_type == "Multiplication":
            response = multiplication_question(operand_a, operand_b)
        elif question_type == "Division":
            response = division_question(operand_a, operand_b)
        elif question_type == "Modulus":
            response = modulus_question(operand_a, operand_b)
        elif question_type == "Exponentiation":
            response = exponentiation_question(operand_a, operand_b)
        elif question_type == "Mix":
            q_types = (addition_question, subtraction_question, multiplication_question, division_question, modulus_question, exponentiation_question)
            response = ra.choice(q_types)(operand_a, operand_b) # pick a random choice from q types, operand a & b to construct the question
        if response:
            print("Correct\n")
            num_of_correct_answers += 1 # num of correct answers will be incremented by 1
        else:
            print("Sorry, incorrect.\n")


def main() -> None:
    """ Driver function that runs the quiz"""
    question_type = choose_question_type()
    if question_type == "Mix":
        print("You will recieve varied questions.\n") # the \n will help break up the large program.
    else:
        print(f"You chose {question_type} questions.\n")

    num_of_questions = choose_number_of_questions()
    print(f"You will be answering {num_of_questions} questions.\n")

    difficulty_level = choose_difficulty_level()
    print(f"You have opted for: {difficulty_level}\n")

    correct_answers = main_game_loop(question_type, num_of_questions, difficulty_level)
    print(f"Quiz finished, with {correct_answers} correct answers out of {num_of_questions}")

# if this file was imported into another file; run main
if __name__ == "__main__":
    main()
