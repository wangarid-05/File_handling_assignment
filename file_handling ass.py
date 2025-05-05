# File Handling and Exception Handling Assignment

def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("Original Content:\n", content)

            # Modify content (e.g., convert to uppercase)
            modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"\nModified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"❌ Error: Unable to read from '{input_filename}' or write to '{output_filename}'.")


def main():
    print("📁 File Read & Write Challenge + 🧪 Error Handling Lab")
    input_filename = input("Enter the name of the file to read: ")
    output_filename = "modified_" + input_filename

    read_and_modify_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
