# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

Numbers = []

while True:

    Put_Numbers = input("Enter The Number's Here To Quite Press Enter: ")

    
    if Put_Numbers == "":
        break

    try:
        one_more = int(Put_Numbers)
        Numbers.append(one_more)       
    except ValueError:
        
        print("please put a valid value")

Numbers.sort(reverse=True)


big5 = Numbers[:5]

small5 = Numbers[-5:]

print("Biggest 5 Num... is")
for number in big5:
    print(number)

print("smaller 5 Num... is")
for number in small5:
    print(number)