#create a program capable of displaying quantities to the user like kbc
# use list data types to store the questions and answers
# display the first amount of person is taking home after playing the game
questions = ["What is the capital of France?", "What is 2 + 2?", "Who wrote 'Romeo and Juliet'?"]
answers = ["Paris", "4", "Shakespeare"]
options = [["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
           ["A. 3", "B. 4", "C. 5", "D. 6"],
           ["A. Dickens", "B. Twain", "C. Shakespeare", "D. Austen"]]
amounts = [1000, 2000, 3000]  # Amounts for each question
print("Welcome to the KBC Game!")
print("You will be asked 3 questions. Answer correctly to win money!")
print("Let's start the game!")
print("You are currently taking home: $0")
print("Question 1: " + questions[0])
print("Options: " + ", ".join(options[0]))
questions = ["What is the capital of France?", "What is 2 + 2?", "Who wrote 'Romeo and Juliet'?"]
options = [["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
           ["A. 3", "B. 4", "C. 5", "D. 6"],
           ["A. Dickens", "B. Twain", "C. Shakespeare", "D. Austen"]]
amounts = [10000, 20000, 30000]  # Amounts for each question
given_answer = input("Your answer (A/B/C/D): ")
given_answer = given_answer.upper()  # Convert to uppercase for comparison