FILE_NAME = "log.txt"

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

update_line()