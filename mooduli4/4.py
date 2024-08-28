#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, 
#kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random 
x =int(random.choice([1,2,3,4,5,6,7,8,9,10]))
y = x
G=(int(input("Guess  the number here: ")))
while G != y :
    if G < y:
        print("Too little guess")
        G=(int(input("Guess  the number here: ")))    
    
    elif G > y:
        print("Too much guess")
        G=(int(input("Guess  the number here: ")))
    
else:
    print("you win")