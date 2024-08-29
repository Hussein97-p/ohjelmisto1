#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
# Käytä for-toistorakennetta.
import random
x = int(input("Throw  Rolls As mush as you want...: "))
y = 0
for i in  range(x):
    D = random.randint(1, 6)
    y = y + D 


print("total dice rolls", y)