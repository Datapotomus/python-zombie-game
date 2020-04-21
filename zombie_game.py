from sys import exit
from sys import argv

"""
My Python game

Building an interactive game much like how the one in ex35 works. However it has to be my own flavor of game.

Outline:
Night of the living dead game
* Start

* Starting choice: You see a shadowy figure in the distance. 
Stay put or go towards figure or walk away


** Features Health Bar - Should probably be the while loop.

"""

health=10
armor=0
attack_rating=1

def show_stats():
    print("====Current Stats====")
    print("Health:", health)
    print("Armor:", armor)
    print("Attack:", attack_rating)
    print("=====================")
    print()


def look_around():
    show_stats()
    print("look_around Placeholder")


def start_walking():
    show_stats()
    print("start_walking Placeholder")


def sit_down():
    show_stats()
    print("You sit down for a minute to get your bearings.")
    global health
    health+=1
    print("You got one extra health, your health is now", health)
    show_stats()
    print("You now have a choice to make do you get up, or keep sitting?")
    choice=input("> ")

    if "sit" in choice:
        dead("A shadowy figure grabs you, and starts eating your flesh. You can't escape.")


def dead(why):
    print(why, "You're DEAD!")
    exit(0)


def start():
    print("You walk up not know where you are.")
    print("Everything is a bit hazy.")
    print("You have a couple of options.")
    print("You can look around, sit down, or just start walking.")

    choice=input("> ")
    if "look" in choice:
        look_around()
    elif "walk" in choice:
        start_walking()
    elif "sit" in choice:
        sit_down()
    else:
        dead("You made the wrong choice.")


start()