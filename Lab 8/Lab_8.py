# Yaroslav Rastopsha - First Student

# Let's create a text file and write some data to it
try:
    with open('students_questions.txt', 'w', encoding='utf-8') as file:
        # Writing my last name
        file.write("Yaroslav Rastopsha\n")
        # Writing a question for the next student
        file.write("Question: How do you handle exceptions when opening a file in Python?\n")
    print("File successfully created and written!")
except Exception as e:
    # Handling any errors that may occur during file operations
    print(f"An error occurred while working with the file: {e}")
