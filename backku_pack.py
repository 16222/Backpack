backpack = []
conditional = "a"
addThing = "a"
removeThing = "a"

while True:
    if len(backpack) > 0:
        print("Here are the items in your backpack:")
        for i in range(len(backpack)):
            print("\n#" + str(i+1) + ",", backpack[i])
    else:
        print("There are no items in your backpack.")
    conditional = str(input("Would you like to add something to your backpack, or remove something? "))
    if conditional.lower().strip() == "add":
        print("\n")
        addThing = str(input("What would you like to add? To go back, please enter 0. "))
        if addThing == "0":
            continue
        else:
            backpack.append(addThing)
    elif conditional.lower().strip() == "remove":
        print("\n")
        if len(backpack) == 0:
            print("There isn't anything to remove.")
            continue
        try:
            removeThing = int(input("To remove something, enter the corresponding number to the item in your backpack. To go back, please enter 0. "))
            if removeThing == "0":
                continue
            del backpack[removeThing-1]
        except:
            print("Either that is a letter, or there is no item with that number attached to it.")
    else:
        print("That's not a valid command.")
        print("\n")
        continue
