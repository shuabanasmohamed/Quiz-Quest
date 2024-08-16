def welcome_message():
    print("Welcome to the Python Quiz!")

def display_question(index, question, options):
    print(f"\nQuestion {index + 1}: {question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def get_user_input():
    while True:
        try:
            answer = int(input("Please enter the number of your answer: "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Invalid input, please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input, please enter a number.")

def calculate_score(answers, correct_answers):
    return sum(1 for user_answer, correct_answer in zip(answers, correct_answers) if user_answer == correct_answer)

def display_results(score, total_questions):
    print(f"\nYour total score is: {score}/{total_questions}")
    if score == total_questions:
        print("Excellent! You got all the questions right.")
    elif score > total_questions / 2:
        print("Good job! You passed.")
    else:
        print("Better luck next time.")

def thank_you_message():
    print("\nThank you for taking the quiz!")

def main():
    questions = [
        ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"]),
        ("What is the largest planet in our Solar System?", ["Earth", "Mars", "Jupiter", "Saturn"]),
        ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"]),
        ("What is the chemical symbol for water?", ["O2", "H2O", "CO2", "N2"]),
        ("What is the square root of 64?", ["6", "7", "8", "9"]),
    ]
    
    correct_answers = [3, 3, 1, 2, 3]  # Correct answers are represented by the index of the correct option

    welcome_message()
    user_answers = []
    for index, (question, options) in enumerate(questions):
        display_question(index, question, options)
        answer = get_user_input()
        user_answers.append(answer)

    score = calculate_score(user_answers, correct_answers)
    display_results(score, len(questions))
    thank_you_message()

if __name__ == "__main__":
    main()