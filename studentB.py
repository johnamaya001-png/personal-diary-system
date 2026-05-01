FILE_NAME = "log.txt"

def append_data():
    print("Enter entries to append. Type 'done' when finished.")
    
    with open(FILE_NAME, "a") as file:
        while True:
            entry = input("Enter entry: ")
            if entry.lower() == "done":
                break
            file.write(entry + "\n")
    
    print("Entries appended successfully.")

def main():
    append_data()

main()