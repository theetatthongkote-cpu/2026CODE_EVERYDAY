# Day 22
# Yen to baht conversion and vice versa pt.2


def yen_to_baht(yen):
    rate = 0.24  # 1 JPY ≈ 0.24 THB (approx)
    return yen * rate


def baht_to_yen(baht):
    rate = 1 / 0.24
    return baht * rate


while True:
    print("\n--- Currency Converter 💱 ---")
    print("1. Yen → Baht")
    print("2. Baht → Yen")
    print("3. Escape")
    choice = int(input("Choose an option (1, 2, or 3): "))
    if choice == 1:
        amount = float(input("Enter amount in Japanese Yen: "))
        result = yen_to_baht(amount)
        print(f"{amount} JPY is approximately {result:.2f} THB")
    elif choice == 2:
        amount = float(input("Enter amount in Thai Baht:"))
        result = baht_to_yen(amount)
        print(f"{amount} THB is approximately {result:.2f} JPY")
    elif choice == 3:
        print("See ya later aligator🐊")
        break
    else:
        print("Invalid Input❌")
