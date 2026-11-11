import os
import time
def clear_screen():
    # Clear the console screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

#establish pet moods
pet_neutral = r"""
 /\_/\\
( o.o )
 > ^ <
 """
pet_happy = r"""
 /\_/\\
( ^.^ )
 > ^ <
 """
pet_uneasy = r"""
 /|_|\
( o.O ) 
 > ^ <
"""
pet_sick = r"""
 /|_|\
( x.x ) 
 > ^ <
"""
pet_name = "Daisy"
print("Welcome to Pocket Pet!")
print("Your kitten's name is " + pet_name)
print(pet_neutral + pet_happy + pet_uneasy)

print("Daisy is a virtual pet that you can interact with. You can play with her, feed her, and put her to sleep. Take care of her and keep her happy!")
input("Press ENTER to start...")
#Daisy initial stats
fullness = 50
happiness = 50
health = 50

#Menu to interact with Daisy and consequences of actions
def show_mood():
    if fullness < 30:
        print(pet_uneasy)
    elif happiness < 30:
        print(pet_neutral)
    elif health < 30:
        print(pet_sick)
    else:
        print(pet_happy)
last_update = time.time()
playing = True
while playing:
    clear_screen()
    current_time = time.time()
    if current_time - last_update >= 60:  # Update every 60 seconds
        fullness = max(0, fullness - 5)  # Decrease fullness by 5, but not below 0
        happiness = max(0, happiness - 5)  # Decrease happiness by 5, but not below 0
        health = max(0, health - 5)  # Decrease health by 5, but not below 0
        last_update = current_time

    show_mood()

    print("What would you like to do with Daisy?")
    print("1. Play with Daisy")
    print("2. Feed Daisy")
    print("3. Put Daisy to sleep")
    print("4. Check Daisy's stats")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        happiness = max(0, min(100, happiness + 10))  # Ensure happiness stays within 0-100
        fullness = max(0, min(100, fullness - 5))  # Ensure fullness stays within 0-100
        health = max(0, min(100, health - 10))  # Ensure health stays within 0-100
        print("You played with Daisy! Happiness increased, but fullness and health decreased.") 
        input("Press ENTER to continue...")
    elif choice == "2":
        fullness = max(0, min(100, fullness + 10))  # Ensure fullness stays within 0-100
        happiness = max(0, min(100, happiness - 5))  # Ensure happiness stays within 0-100
        print("You fed Daisy! Fullness increased and happiness decreased.")
        input("Press Enter to continue...")
    elif choice == "3":
        health = max(0, min(100, health + 10))  # Ensure health stays within 0-100
        print("You put Daisy to sleep! Health increased.")
        input("Press Enter to continue...")
    elif choice == "4":
        print(f"Daisy's stats - Fullness: {fullness}/100, Happiness: {happiness}/100, Health: {health}/100")
        input("Press ENTER to continue...")
    elif choice == "5":
        playing = False
        print("Thanks for playing with Daisy!")
        print(r"""
             //\_/\\
            (//^.^//)
             >  ♡  <
            """)
    else:
        print("Invalid choice. Try again!")

    #Daisy Conditions
    mood = pet_happy

    if fullness < 30:
        mood = pet_uneasy

    if happiness < 30:
        mood = pet_neutral

    if health < 30:
        mood = pet_sick

    history = []

    history.append("You played with Daisy! Happiness increased, but fullness decreased.")
    history.append("You fed Daisy! Fullness increased and happiness decreased.")
    history.append("You put Daisy to sleep! Health increased.")

    print("Daisy's Journal:")
    for interaction in history:
        print(interaction)