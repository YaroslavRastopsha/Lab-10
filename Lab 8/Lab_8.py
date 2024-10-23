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
    
    # Maksym Grigorenko - Second Student

# Let's open the file created by the first student and append our data
try:
    with open('students_questions.txt', 'a', encoding='utf-8') as file:
        # Writing my last name
        file.write("Maksym Grigorenko\n")
        # Writing the answer to the previous student's question
        file.write("Answer: In Python, exceptions are handled using the try-except block.\n")
        # Adding my question for the next student
        file.write("Question: What is the difference between lists and tuples in Python?\n")
    print("File successfully updated with my data!")
except Exception as e:
    # Handling any errors that may occur during file operations
    print(f"An error occurred while working with the file: {e}")

