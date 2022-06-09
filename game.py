import random

def mygame(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you=="p":
            return False
        elif you == "r":
            return True
    elif comp == "p":
        if you=="r":
            return False
        elif you == "s":
            return True
    elif comp == "r":
        if you=="s":
            return False
        elif you == "p":
            return True




print("Comp turn: rock(r) paper(p) and Scissors(s) :- ")
random = random.randint(1, 3)

if random == 1:
    comp = 'r'
elif random == 2:
    comp = "p"
elif random == 3:
    comp = "s"



you = input("Player 2 turn: Snake(s) Water(w) and Gun(g) :- ")
print(f"Computer chocie {comp}")
print(f"you chocie {you}")
a = mygame(comp, you)
if a == None:
    print("This game is tie!")
elif a == True:
    print("You win!")
else:
    print("You lose!")

