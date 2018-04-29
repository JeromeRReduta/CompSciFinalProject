# Say you win the game
winCondition = True
# Game Over Message, asking to restart game
def gameOver():
    print("You won!")
    print("This was a cool game. Now it's done.")
    again = input("Keep going? [1] Anotha One [2] Quit ")
    if again == "2":
        return False


# If user wants to quit, loop breaks. Otherwise, loop restarts
while True:
    # Insert game here
    if winCondition == True:
        gameOver()
    if gameOver() == False:
        print("Bye")
        break
