import os

def modify_content(content):
    """
    Modify the content of the file. This is an example; you can customize it.
    """
    return content.upper()

def main():
    # Ask user for input file name
    input_filename = input("Enter the name of the file to read: ").strip()

    try:
        # Check if file exists
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"File '{input_filename}' does not exist.")

        # Read the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Generate a new output filename
        output_filename = f"modified_{input_filename}"

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"The modified content has been written to '{output_filename}'.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{input_filename}'.")
    except OSError as e:
        print(f"I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the file processing tool.")

if __name__ == "__main__":
    main()
