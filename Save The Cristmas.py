name = input("Enter Your Name : ")
print("\n\n\n\n Hello, " + name + "\n\n\tWelcome")

print("""
      You are the one of the elfs of Santa, a bad wizard stole Cristmas gifts and unfortunatety you were sleeping inside of 
      the Santa`s gifts bag that is why wizard kidnapped you by mistake, you scared but then you realised this is a huge opportunity 
      for you, if you can save the christmas gift and bring them back to the Santa you can be a hero, you've taken bag and started to move, 
      you see possible 3 door to go out from wizard's room, which one do you choose?  --- 1, 2 or 3 ?""")

door = input(">")

if(door == "1"):
    print("\n" * 10)
    print("You entered the First room and teleported another age you found yourself in a an ancient Battle")
    print("By looking at the Flag of an soldier you understood that\nIt is the battle of Spartans")
    print("You hide in the bush and found a Sword lying on the ground")
    print("What would you do?")
    print("1-Pick the Sword and Run from the Battleground")
    print("2-Pick the Sword and Fight for your life")

    options = input(">")
    if(options == "1"):
        print("\n\n\n\nAs you started running\nomeone from back hit you with the Arrow!\nYou are dead.\nGAME OVER")
    elif(options == "2"):
        print("\n\n\n\n You started fighting from the spartans side, \nluckily you survived the battlefield and lived the rest of the life as a commander in the Army\nYou stucked in the past for the rest of your life\nGAME OVER")
    else:
        print("GAME OVER\nPLEASE RESTART the GAME")

if(door == "2"):
    print("\n" * 10)
    print("You entered the Second room and found yourself in a jungle with an ancient map near of you")
    print("The Map contains a route leading to a treasure hidden in the forest")
    print('What would you do?')
    print("1-Wait for the help.")
    print("2-Find for an exit on on your own.")
    print("3-Take the Map.")

    forest = input(">")
    if(forest == "1"):
        print("\n\n\n\nNo one was there to help you.\nYou hide from the wild animals for a while.\nGot killed by the Wolf in the End\nGAME OVER")
    elif(forest == "2"):
        print("\n\n\n\nYou look for an exit in jungle on your own.\nIn the pain of hunger you ate poisoned berries.\nGood job! You Died!\nGAME OVER")
    elif(forest == "3"):
        print("\n\n\n\nYou followed the Map, discovered some beautiful views of deep forest.\nFinally reached the treasure chest.\nYou opened the chest but it was empty")
        print("You got disappointed\nAfter walking for a while.\nYou saw a river and sat near the river and relaxed. Then you have found the exit\n###You Won the Game###")
    else:
        print("GAME OVER\nPLEASE RESTART the GAME")
if (door == "3"):
    print("\n\n\n\nYou entered the Third room and found yourself in front of a Witch who is boiling Potions")
    print("She asked how did you enter here? What are you? A dwarf child?")
    print("What will you answer-")
    print("1-Yes, i am a dwarf child and i am lost, and want to get out of here.")
    print("2-you got angry and said <I am a elf, you big bad witch!!> and You stab her with a knife.")
    print("3-You try to runaway.")

    witch = input(">")
    if(witch == "1"):
        print("\n\n\n\nShe cast a spell on you and you become unconscious.")
        print("She brewed you into her boiling potion pot")
        print("Good bye! You Died\nGAME OVER")
    elif(witch == "2"):
        print("\n\n\n\nYou come close to her and swung your knife at her face and then killed her.")
        print("Good job. You found the exit, You saved the Cristmas.\nBut You are a killer now!\n###But You Won the Game###")
    elif(witch == "3"):
        print("\n\n\n\nShe casts a spell that freezes you in place.")
        print("She prisoned you in her cabin.")
        print("Good job! You became her slave for the rest of your life.")
    else:
        print("GAME OVER\nPLEASE RESTART the GAME")