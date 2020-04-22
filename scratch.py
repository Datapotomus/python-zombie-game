health=10
print("Health currently is:", health)
def addhealth(points):
    global health
    health += int(points)

healthpoints=input("> ")

addhealth(healthpoints)

print("health after assignment is:", health)