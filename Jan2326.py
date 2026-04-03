# Day 23
# Adding Yuan
def yen_to_baht(yen):
    rate = 0.24  # 1 JPY ≈ 0.24 THB (approx)
    return yen * rate


def baht_to_yen(baht):
    rate = 1 / 0.24
    return baht * rate


def yuan_to_baht(yuan):
    return yuan * 4.95


def baht_to_yuan(baht):
    return baht / 4.95


while True:
    try:
        choice = int(input("Choose an option (1–5): "))
    except ValueError:
        print("Please enter a number ❌")
        continue

    if choice == 1:
        amount = float(input("Enter Yen: "))
        print(f"{amount} JPY ≈ {yen_to_baht(amount):.2f} THB")

    elif choice == 2:
        amount = float(input("Enter Baht: "))
        print(f"{amount} THB ≈ {baht_to_yen(amount):.2f} JPY")

    elif choice == 3:
        amount = float(input("Enter Yuan: "))
        print(f"{amount} CNY ≈ {yuan_to_baht(amount):.2f} THB")

    elif choice == 4:
        amount = float(input("Enter Baht: "))
        print(f"{amount} THB ≈ {baht_to_yuan(amount):.2f} CNY")

    elif choice == 5:
        print("Peace ✌️ Safe travels in Japan 🇯🇵")
        break

    else:
        print("Invalid option ❌")
