# error_handling_lab.py
# Lab: Handle file not found or unreadable cases

def error_handling():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            print("\n📖 File Content:")
            print(f.read())

    except FileNotFoundError:
        print(f"⚠️ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"🚫 Error: No permission to read '{filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    error_handling()
