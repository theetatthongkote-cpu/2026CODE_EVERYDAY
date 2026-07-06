# Day 87
# learning about csv files(BRO CODE on youtube)
# + learning about how machines and gpts work.
# i will be focusing on the porject tmr and organize the code
# https://www.youtube.com/watch?v=GRNI9T9R8gQ&list=TLPQMjgwMzIwMjZcnVc2T_AhBA&index=2
# https://www.youtube.com/watch?v=5sLYAQS9sWQ&list=TLPQMjgwMzIwMjZcnVc2T_AhBA&index=3
# https://www.youtube.com/watch?v=qYNweeDHiyU&list=TLPQMjgwMzIwMjZcnVc2T_AhBA&index=4

import csv
BBALL_PLAYERS_INFO = [["Name", "Position", "Rings"],
                      ["LeBron James", "Small Forward", "4"],
                      ["Stephen Curry", "Point Guard", "4"],
                      ["Kawhi Leonard", "Small Forward", "2"]
                      ]

FILE_PATH = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\output.csv"


try:
    with open(FILE_PATH, "w", endline=" ") as f:
        writer = csv.writer(f)
        for row in BBALL_PLAYERS_INFO:
            writer.writerow(row)
        print(f"csv file {FILE_PATH} was created")
except IOError:
    print("File already exists")
