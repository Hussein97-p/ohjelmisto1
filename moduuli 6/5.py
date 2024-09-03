
#اكتب دالة تأخذ قائمة من الأعداد الصحيحة كمعلمة.
#يقوم البرنامج بإرجاع قائمة أخرى 
#والتي تشبه القائمة التي تم تلقيها كمعلمة، باستثناء أنه تمت إزالة جميع الأرقام الفردية منها.
#للاختبار، اكتب برنامجًا رئيسيًا تقوم فيه بإنشاء قائمة، 
#واستدعاء دالة، ثم طباعة كل من القائمة الأصلية والقائمة المقتطعة.

#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
#Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois
#kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, 
#jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def just_even (list):
    Right_list = []
    for Even in list:
        if Even % 2 == 0 :
            Right_list.append(Even)
    return Right_list

list = []
for i in range(5):
    x = int(input("Put The Number's Here: "))
    list.append(x)
    print(list)
        
print("The Orginal LIst is: " , list)
DO_it = just_even(list)
print ("The List Where Just Even Number's", DO_it)