import random

rock = "rock"
paper = "paper"
scissor = "scissor"

gamestart = int(input("press 1 to play the game, press 2 to quit: "))

while gamestart == 1:

    game = random.randrange(0,3)

    char1 = int(input("select 1,2,3 based on rock, paper or scizzor:\n "))

    print("you choose\n")

# if char1 == 1:
#     print(rock)
# elif char1 == 2:
#     print(paper)
# elif char1 == 3:
#     print(scissor)


# if game == 1:
#     print(rock)
# elif game == 2:
#     print(paper)
# else:
#     print(scissor)

# it can also bee written as
    gamech = [rock, paper, scissor]

    print(gamech[char1])
    print("\ncomputer choose\n")
    print(gamech[game])




    if game == char1:
        print("its a tie")
    elif game == 0 and char1 == 1:
        print("you win")
    elif game == 1 and char1 == 2:
        print("you win")
    elif game == 2 and char1 == 0:
        print("you win")
    elif char1 > 2 or char1 < 0:
        print("its an invalid number")
    else:
        print("you lose")

    gamestart = int(input("\nwant to play another round press 1 to start and 2 to stop: "))
print("game stopped")



