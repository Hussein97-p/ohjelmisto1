#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
# (Oikea käyttäjätunnus on python ja salasana rules)
Times = 5
time = 0
while  time < Times:

    U_ser = str(input("Enter The User Name: "))
    Password = str(input("Enter The Password: "))

    if (U_ser != "pyhon") and (Password != "rules"):
        print("user name or password is't Correct")
        Times -= 1 
        if Times == 0:
            print("The attempts are over.")
        print("Remaining attempts" ,Times)

    else:
        print("Welcome you..")
        break

if time == Times:
    print("Access failed")
