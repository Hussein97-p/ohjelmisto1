#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
#Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
#syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
#Käytä joukkotietorakennetta nimien tallentamiseen.
#-----------------------------------------------------------------------------------------------------------------------------------------------
#اكتب برنامجًا يطالب المستخدم بالأسماء حتى يقوم المستخدم بإدخال سلسلة فارغة.
#بعد إدخال كل اسم، يقوم البرنامج بطباعة إما النص اسم جديد أو الاسم الذي تم إدخاله مسبقًا،
#اعتمادًا على ما إذا كان الاسم قد تم إدخاله لأول مرة.
#وأخيراً يقوم البرنامج بسرد الأسماء المدخلة واحداً تلو الآخر بترتيب عشوائي. استخدم بنية بيانات الصفيف لتخزين الأسماء.
#-----------------------------------------------------------------------------------------------------------------------------------------------
import random

Name_s = []

set_name = set()

while True:
    
    x = input("Put The Name's Here (or press Enter to finish): ")
    
    if x == "":
        break
    
    
    if x in set_name:
        print("It's already there")
    else:
        print("New name")
        set_name.add(x)   
        Name_s.append(x)  

random.shuffle(Name_s)

print(" ".join(Name_s))