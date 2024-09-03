#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
#Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
#Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
#joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random
def i_do (y):
    while True:
        x = random.randint(1,y)
        if x == y :
            print("Here you go", x)
            break
        else:
            print (x)

y = int(input("Put the number you want: "))
i_do (y)


