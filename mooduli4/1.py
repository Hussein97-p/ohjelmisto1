#4. Alkuehdollinen toistorakenne (while)
#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

Num_ber = 1 
while Num_ber < 1000: 
    Num_ber = Num_ber + 1
    if Num_ber %3 == 0 :
        print(Num_ber)
