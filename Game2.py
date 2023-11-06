#Author Oxt4n1nc9b4r 
import random

def math_quiz():
    print("Welcome to the Brain Game: Math Quiz!")
    score = 0
    total_questions = 5  # You can adjust the number of questions

    for _ in range(total_questions):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*', '/'])

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        else:
            result = num1 / num2

        user_answer = float(input(f"What is {num1} {operator} {num2}? "))
        
        if user_answer == result:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {result}")

    print(f"You got {score} out of {total_questions} questions correct. Great job!")

if __name__ == "__main__":
    math_quiz()
