#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina 
#ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, 
#joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. 
#Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa. 

def convert ():
    while True:
        US_gallons = float (input(("If you put a Negative value the program will stop)\nPut The Us Gallons Here To Convert: ")))
        lit_ers =US_gallons * 3.785 
        if US_gallons >= 1 :
            print (lit_ers)
        else:
            print("Fall")
            break


convert()