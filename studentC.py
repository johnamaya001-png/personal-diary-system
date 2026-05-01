def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            print("File Content:\n")
            
            for line in lines:
                print(line.strip())
            
            print("\nTotal number of lines:", len(lines))
    
    except FileNotFoundError:
        print("Error: File not found.")
    
    except Exception as e:
        print("An error occurred:", e)


# Example usage
filename = "data.txt"
count_lines(filename)