# Day 24
# sleepy coding
def yen_to_baht(yen):
    return yen * 0.24


def baht_to_yen(baht):
    return baht / 0.24


country = input("Where are you right now? (Japan/Thailand): ").lower()

if country == "japan":
    yen = float(input("How much Yen do you have? "))
    print(f"That's about {yen_to_baht(yen):.2f} THB 🇹🇭")

elif country == "thailand":
    baht = float(input("How much Baht do you have? "))
    print(f"That's about {baht_to_yen(baht):.2f} JPY 🇯🇵")

else:
    print("I don't know that country yet 😅")
