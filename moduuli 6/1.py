#اكتب دالة بدون معلمات تُرجع كقيمة
# إرجاع رقم نرد عشوائي بين 1..6.
# اكتب برنامجًا رئيسيًا يرمي فيه النرد حتى يظهر الرقم ستة.
# يقوم البرنامج الرئيسي بطباعة عدد الغرز التي تم الحصول عليها بعد كل لفة.
#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
#Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
def nard():
    return random.randint(1,6)
x = nard()
print(x)

#---------------------------------------------------------------------------------------------#
import random
def To_check ():
    while True:
        x = random.randint(1,6)
        if x == 6:
            print("Here is your number: " , x )
            break
        else:
            print(x)

To_check()