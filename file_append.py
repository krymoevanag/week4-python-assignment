# Specify the file name
file_name = "sample_file.txt"

# Content to append
content_to_append = "\nEvans Kirimi is constantly expanding his knowledge in programming and technology."

# Open the file in append mode and write content
with open(file_name, "a") as file:
    file.write(content_to_append)

print(f"Content appended successfully to {file_name}.")
