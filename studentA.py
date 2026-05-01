FILE_NAME = "log.txt"

def create_file():
    try:
        with open(FILE_NAME, "x") as file:
            print("File created successfully.")
    except FileExistsError:
        print("File already exists.")

def write_initial_data():
    data = input("Enter initial data for the file: ")
    
    with open(FILE_NAME, "w") as file:
        file.write(data + "\n")
    
    print("Initial data written successfully.")

def main():
    create_file()
    write_initial_data()

# Run program
main()