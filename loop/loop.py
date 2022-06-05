# This is for the FOR loop
names = ["Ram", "Sita", "Gita"]
for item in names:
    print("The name of this preson is", item)


for i in range(1, 10, 5):
    print(i)
else:
    print("this is wrong")    





# This is FOR WHILE loop
run = True
current = 1
while run:
    if current == 10:
        run = False
    else:
        print(current)
        current += 1