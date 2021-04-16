print("Average speed in km/h")
km = input()
print("What was the speed limit?")
limit = input()

if int(km) <= int(limit):
    print("OK")
elif int(km) == int(limit) + 5:
    print("1 point")

elif int(km) == int(limit) + 10:
    print("2 points")

elif int(km) == int(limit) + 15:
    print("3 points")

elif int(km) == int(limit) + 20:
    print("4 points")

elif int(km) == int(limit) + 25:
    print("5 points")

elif int(km) == int(limit) + 30:
    print("6 points")

elif int(km) == int(limit) + 35:
    print("7 points")

elif int(km) == int(limit) + 40:
    print("8 points")

elif int(km) == int(limit) + 45:
    print("9 points")

elif int(km) == int(limit) + 50:
    print("10 points")

elif int(km) == int(limit) + 55:
    print("11 points")

elif int(km) == int(limit) + 60:
    print("12 points")

else:
    print(" Time to go to jail")
