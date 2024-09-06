#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)
#---------------------------------------------------------------------------------------------------------------------------
#كتابة برنامج لاسترجاع وتخزين معلومات المطار. يسأل البرنامج المستخدم إذا كان يريد الدخول إلى مطار جديد، 
# أو استرجاع معلومات المطار الذي دخله بالفعل، 
# أو التوقف. إذا اختار المستخدم الدخول إلى مطار جديد، يطلب البرنامج من المستخدم رمز واسم المطار الخاص بمنظمة الطيران المدني الدولي 
# (ICAO). إذا اختار المستخدم البحث، يطلب البرنامج رمز منظمة الطيران المدني الدولي ويطبع اسم المطار المقابل.
#-----------------------------------------------------------------------------------------------------------------------------------------------
All_Airport = {}

while True:
    A = "(A) Do You Want To Enter To A New Airport: "
    B = "(B) Do You Want To Return Any Airport Info You Have Visited Before: "
    C = "(C) Stop The Program."
    print(A, "\n", B, "\n", C)
    x = input("Choose One Of The Options Above: ").upper()
    
    if x == "C":
        print("Thank you!")
        break
    elif x == "B":

        key = input("Enter the ICAO code of the airport you want to retrieve: ").upper()
        if key in All_Airport:
            print(f"ICAO Code: {key}, Airport Name: {All_Airport[key]}")
        else:
            print("The Airport not found.")
    elif x == "A":

        key = input("Enter the ICAO code of the airport Here: ").upper()
        Name_airport = input("Enter the name of the airport Here: ")

        All_Airport[key] = Name_airport
        print(f"Airport added: ICAO Code: {key}, Airport Name: {Name_airport}")
    else:
        print("Invalid choice. Please select option A, B, or C.")