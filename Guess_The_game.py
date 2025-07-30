import random

target = random.randint(1,100)

print("\n🎉Welcome to the Guess the number game💡\n")
while True:
    Userchoice = input("\n🤔Enter your guess (1-10) or Quit press Q: \n")
    if(Userchoice=="Q"):
        break

    Userchoice = int(Userchoice)
    if (Userchoice==target):
        print("\n✅ Correct!: You Win The Game🏆🎊\n")
        break
    elif (Userchoice < target):
        print("\n❌Your Number Was too small🔽.Take Bigger Guess🔁")

    else:
        print("\n❌Your Number Was too Big🔼. Take Smaller Guess🔁")


print("\n------------------------💀Game Over💀--------------------------\n")