# day 170
# today ill be making my first python script!
from pathlib import Path

file_path = Path("C:\\Users\\Public\\Desktop\\script.txt")

if file_path.exists():
    print("Stop! This file already exists. I won't overwrite it.")
else:
    # 3. Ask the user what to write
    text = input("Type something to save inside your file: ")

    # 4. Open, write, and safely close the file automatically
    with open(file_path, "w") as file:
        file.write(text)

    print("Success! Your file has been created.")
