num = int(input("Enter the number"))
for i in range(1, 11):
    print(str(num) + "X" + str(i) + "=" + str(i*num))
    print(str(i*num))





l1 = ["Hari", "Surendra", "Sujan", "Rahul"]
for name in l1:
    if name.startswith("S"):
        print("Hello "  + name)
    else:
        quit
