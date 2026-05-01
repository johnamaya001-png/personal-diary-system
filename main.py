FILE_NAME = "log.txt"

def create_file():
    try:
        with open(FILE_NAME, "x") as file:
            print("File created successfully.")
    except FileExistsError:
        print("File already exists.")

def write_initial_data():
    data = input("Enter initial data: ")
    with open(FILE_NAME, "w") as file:
        file.write(data + "\n")
    print("Initial data written.")

def append_data():
    data = input("Enter data to append: ")
    with open(FILE_NAME, "a") as file:
        file.write(data + "\n")
    print("Data appended.")

def read_file():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
            print("\n--- File Content ---")
            for line in lines:
                print(line.strip())
            print(f"\nTotal lines: {len(lines)}")
    except FileNotFoundError:
        print("File not found.")

# STUDENT D - update specific line
def update_line():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            print(f"{i+1}: {line.strip()}")

        line_num = int(input("Enter line number to update: "))
        new_data = input("Enter new data: ")

        if 1 <= line_num <= len(lines):
            lines[line_num - 1] = new_data + "\n"

            with open(FILE_NAME, "w") as file:
                file.writelines(lines)

            print("Line updated successfully.")
        else:
            print("Invalid line number.")

    except FileNotFoundError:
        print("File not found.")

# BONUS - search
def search_data():
    keyword = input("Enter keyword to search: ")
    try:
        with open(FILE_NAME, "r") as file:
            found = False
            for line in file:
                if keyword.lower() in line.lower():
                    print("Found:", line.strip())
                    found = True
            if not found:
                print("No match found.")
    except FileNotFoundError:
        print("File not found.")

# BONUS - delete line
def delete_line():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            print(f"{i+1}: {line.strip()}")

        line_num = int(input("Enter line number to delete: "))

        if 1 <= line_num <= len(lines):
            del lines[line_num - 1]

            with open(FILE_NAME, "w") as file:
                file.writelines(lines)

            print("Line deleted.")
        else:
            print("Invalid line number.")

    except FileNotFoundError:
        print("File not found.")


# MAIN MENU
def main():
    while True:
        print("\n==== PERSONAL DIARY SYSTEM ====")
        print("1. Create File (A)")
        print("2. Write Initial Data (A)")
        print("3. Append Data (B)")
        print("4. Read File (C)")
        print("5. Update Line (D)")
        print("6. Search Data")
        print("7. Delete Line")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_initial_data()
        elif choice == "3":
            append_data()
        elif choice == "4":
            read_file()
        elif choice == "5":
            update_line()
        elif choice == "6":
            search_data()
        elif choice == "7":
            delete_line()
        elif choice == "8":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")
# Run program
main()