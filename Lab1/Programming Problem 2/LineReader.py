def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return

    num_lines = len(lines)
    print(f"The file '{filename}' has {num_lines} lines.")

    while True:
        line_num = int(input("Enter a line number (0 to quit): "))
        if line_num == 0:
            break
        elif 1 <= line_num <= num_lines:
            print(f"Line {line_num}: {lines[line_num - 1]}")
        else:
            print(f"Invalid line number: {line_num}")

if __name__ == "__main__":
    main()
