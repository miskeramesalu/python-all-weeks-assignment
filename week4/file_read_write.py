# file_read_write.py
# Challenge: Read from one file and write modified content to another

def file_read_write():
    try:
        with open("input.txt", "r", encoding="utf-8") as infile:
            content = infile.read()

        # Modify content: make uppercase
        modified = content.upper()

        with open("output.txt", "w", encoding="utf-8") as outfile:
            outfile.write("Modified Content:\n")
            outfile.write(modified + "\n")

        print("✅ File read & write challenge completed! Check 'output.txt'.")

    except FileNotFoundError:
        print("⚠️ Error: 'input.txt' not found. Please create it with text.")

if __name__ == "__main__":
    file_read_write()
