# Leah Toutounjian
# HW 6

import random

def add(a, b):
    addition = a + b
    return addition

def subtract(c, d):
    subtraction = c - d
    return subtraction

def multiply(e, f):
    multiplication = e * f
    return multiplication

def divide(g, h):
    division = g / h
    return division

def displayMathQuestion(operator, operandOne, operandTwo):
    print("\n ",operandOne)
    print(operator,operandTwo)
    print("----------")
    print("   ?")
    

def main():
    
    correctAnswerCounter = 0
    wrongAnswerCounter = 0
    questionsTotal = 0
    quiz = "Yes"
    
    while quiz == "Yes":  
    
        quiz = input("\nDo you want to answer a quiz question? (Yes/No): ")
        quiz = quiz.capitalize()
    
        while quiz != "Yes" and quiz != "No":
        
            print("\nInvalid selection! Please enter Yes or No.")
            quiz = input("\nDo you want to answer a quiz question? (Yes/No): ")
            quiz = quiz.capitalize()
            
        if quiz == "No":
            print(f"\nYou answered " + str(questionsTotal) + " questions in total!")
            print(f"\nOut of the " + str(questionsTotal) +" questions you answered, you got " + str(correctAnswerCounter) + " correct!")
            print(f"Out of the " + str(questionsTotal) + " questions you answered, you got " + str(wrongAnswerCounter) + " wrong.")
            
            if questionsTotal > 0: #I spent way too long figuring this out and now I know 0/0 cannot be divided in my code
                percentage_correct = (correctAnswerCounter / questionsTotal) * 100
                print(f"\n Your percentage correct is: {percentage_correct:.2f}%")
    
        elif quiz == "Yes":
        
            operator = random.randint(1,4)
            num1 = random.randint(1,500)
            num2 = random.randint(1,500)
       
            if operator == 1:
                operation = "+"
                correctAnswer = add(num1,num2)
        
            elif operator == 2:
                operation = "-"
                correctAnswer = subtract(num1,num2)
           
            elif operator == 3:
                operation = "*"
                correctAnswer = multiply(num1,num2)

            elif operator == 4:
                operation = "/"
                correctAnswer = divide(num1,num2)
           
            displayMathQuestion(operation, num1, num2)
    
            inputedAnswer = float(input("\nPlease enter your answer to the question above: "))
    
            if inputedAnswer == correctAnswer:
                print("\nGood work! Your answer is correct.")
                correctAnswerCounter = correctAnswerCounter + 1
        
            else:
                print("\nOops! You entered the wrong answer!")
                print(f"\nThe correct answer is: {correctAnswer:,.2f}")
                print("\nDon't worry, you'll get it next time!")
                wrongAnswerCounter = wrongAnswerCounter + 1
    
            questionsTotal = questionsTotal + 1
        
main()
