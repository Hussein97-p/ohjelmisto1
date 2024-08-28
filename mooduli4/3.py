#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

my_list = []


while True:
    nUM_ber =(input("Enter The Numbers Here: "))
    

    if nUM_ber != "":
        my_list.append(int(nUM_ber))
    else:
        break    
    
    big =max(my_list)
    small=min(my_list)
    
print(big)
print(small)