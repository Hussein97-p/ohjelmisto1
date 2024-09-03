#اكتب دالة تستقبل كمعلمات قطر قطعة البيتزا المستديرة بالسنتيمتر وسعر البيتزا باليورو.
#تقوم الدالة بحساب وإرجاع سعر وحدة البيتزا باليورو لكل متر مربع.
#يسأل البرنامج الرئيسي المستخدم عن أقطار وأسعار فطيرتين من البيتزا
#ويشير إلى البيتزا التي تعطي قيمة أفضل مقابل المال (أي أي واحدة لها سعر وحدة أقل)
#يجب استخدام الوظيفة المكتوبة في حساب أسعار الوحدات.
#--------------------------------------------------------------------------------------------------------------#
#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
#Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
#kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
#Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
#---------------------------------------------------------------------------------------------------------------#
#Koska pizza on ympyrä, ympyrän pinta-ala on laskettava
π = 3.14

def sol(d, p):
    return p / (π * (d / 200) ** 2)

x, c = map(float, input("Enter diameter and price of the first pizza\n(put 2 value's\n(press after first value space)): ").split())

y, l = map(float, input("Enter diameter and price of the second pizza\n(put 2 value's\n(press after first value space)): ").split())

p1 = sol(x, c)
p2 = sol(y, l)

print(f"Unit price of the first pizza: {p1:.2f} €")
print(f"Unit price of the second pizza: {p2:.2f} €")
print("The first pizza is better" if p1 < p2 else "The second pizza is better" if p1 > p2 else "Both pizzas are equal")
