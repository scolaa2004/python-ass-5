# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file and write initial content
        with open("my_file.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("54321 is a number.\n")
            file.write("This is the third line.\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating or writing to the file: {e}")

def read_file():
    try:
        # Read and display the contents of the file
        with open("my_file.txt", "r") as file:
            content = file.read()
        print("File contents:\n")
        print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def append_file():
    try:
        # Open the file in append mode and add more content
        with open("my_file.txt", "a") as file:
            file.write("This is an appended line.\n")
            file.write("09876 is another number.\n")
            file.write("Final line after appending.\n")
        print("Additional content appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("File append operation completed.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()  # Display the file content after appending
