# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, 
# jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla


x = int (input("Enter the year here: "))
if (x %4 == 0  and x %100 != 0) or x %400 == 0:
    print("leap year.")
else: print("This Year is't Leap year")
