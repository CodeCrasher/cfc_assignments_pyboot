credit = int(input("Enter the value of credits: "))
if credit >= 7500:
    print("Tera Leader")
elif credit >= 6000 and credit < 7500:
    print("Gega Leader")
elif credit >= 4500 and credit < 6000:
    print("Mega Leader")
elif credit < 4500:
    print("Rising star")
