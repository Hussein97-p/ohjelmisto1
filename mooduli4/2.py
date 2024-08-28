#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
#  Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

while True:
    converts_inches_to_centimeters = float(input("To converts inches to centimeters Put The inches Number Here: "))
    y = converts_inches_to_centimeters * 2.54
    if converts_inches_to_centimeters <=0:
        break
    print(y, "Cm")
