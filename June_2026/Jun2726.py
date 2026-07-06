# day 173
# i went to a swim comp today

# 100m estimator
# formula = (pb50m * 2) + drop-offtime(3, 8)

def status1(user_input):
    user_input = user_input.strip().lower()
    if user_input in ["elite", "e"]:
        return "Elite"
    if user_input in ["club", "c"]:
        return "CLUB"
    raise ValueError("Invalid status")


def calculate(pb50, status):
    drop_off = 3 if status == "Elite" else 8
    return pb50 * 2 + drop_off


def main():
    while True:
        try:
            status = status1(input("Are you an Elite or a CLUB swimmer? \n"))
            pb50m = int(input("Enter ur 50m pb: "))
            print("Estimated 100m time:", calculate(pb50m, status))
            break
        except ValueError:
            print("Please enter a valid status and a numeric 50m PB.")


if __name__ == "__main__":
    main()
