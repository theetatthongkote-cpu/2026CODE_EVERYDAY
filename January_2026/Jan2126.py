# day 21
# Yen to baht conversion and vice versa


def yen_to_baht(yen):
    rate = 0.24  # 1 JPY ≈ 0.24 THB (approx)
    return yen * rate


def baht_to_yen(baht):
    rate = 1 / 0.24
    return baht * rate


yen_amount = float(input("Enter amount in Japanese Yen: "))
baht_result = yen_to_baht(yen_amount)
print(f"{yen_amount} JPY is approximately {baht_result:.2f} THB")


baht_amount = float(input("Enter amount in Thai Baht: "))
yen_result = baht_to_yen(baht_amount)
print(f"{baht_amount} THB is approximately {yen_result:.2f} JPY")
