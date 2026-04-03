# day 9
# file I/O - writing to a file
text_data = "Hello, I am learning about how files work in Python."
file_path = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\text_file.txt"
with open(file_path, 'w') as file:
    file.write(text_data)
    print(f'text_file "{file_path}" created and data written to it.')
with open(file_path, "a") as file:
    file.write("\nI wrote this line after creating the file.")
    print(f'New line written to the file "{file_path}".')
with open(file_path, "r") as file:
    content = file.read()
    print("The content of the file is:", content)
